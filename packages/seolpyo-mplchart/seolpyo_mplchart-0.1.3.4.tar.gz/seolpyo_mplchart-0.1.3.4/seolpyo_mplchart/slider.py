from matplotlib.collections import LineCollection
from matplotlib.backend_bases import MouseEvent, MouseButton, cursors
import pandas as pd


from .cursor import CursorMixin, Chart as CM


class Mixin:
    def on_click(self, e):
        "This function works if mouse button click event active."
        return
    def on_release(self, e):
        "This function works if mouse button release event active."
        return
    def draw_artist(self):
        "This function works before canvas.blit()."
        return


class NavgatorMixin(CursorMixin):
    min_distance = 30
    color_navigatorline = '#1e78ff'
    color_navigator = 'k'

    _x_click, _x_release = (0, 0)
    is_click, is_move = (False, False)
    _navcoordinate = (0, 0)

    def _add_collection(self):
        super()._add_collection()

        # 슬라이더 네비게이터
        self.navigator = LineCollection([], animated=True, edgecolors=[self.color_navigator, self.color_navigatorline], alpha=(0.2, 1.0))
        self.ax_slider.add_artist(self.navigator)
        return

    def _set_data(self, df: pd.DataFrame, sort_df=True, calc_ma=True, change_lim=True, calc_info=True):
        super()._set_data(df, sort_df, calc_ma, change_lim, calc_info)

        # 네비게이터 라인 선택 영역
        xsub = self.xmax - self.xmin
        self._navLineWidth = xsub * 0.008
        if self._navLineWidth < 1: self._navLineWidth = 1
        self._navLineWidth_half = self._navLineWidth / 2
        return

    def _connect_event(self):
        super()._connect_event()
        self.canvas.mpl_connect('axes_leave_event', lambda x: self._leave_axes(x))
        self.canvas.mpl_connect('button_press_event', lambda x: self._on_click(x))
        self.canvas.mpl_connect('button_release_event', lambda x: self._on_release(x))
        return

    def _leave_axes(self, e: MouseEvent):
        if not self.is_click and e.inaxes is self.ax_slider:
            self.canvas.set_cursor(cursors.POINTER)
        return

    def _on_click(self, e: MouseEvent):
        if self.is_click or e.button != MouseButton.LEFT or e.inaxes is not self.ax_slider: return

        self.is_click = True

        x = e.xdata.__int__()
        left, right = self._navcoordinate
        lmin, lmax = (left-self._navLineWidth, left+self._navLineWidth_half)
        rmin, rmax = (right-self._navLineWidth_half, right+self._navLineWidth)

        gtl, ltr = (lmax < x, x < rmin)
        if gtl and ltr:
            self._x_click = x
            self.is_move = True
            self.canvas.set_cursor(cursors.MOVE)
        else:
            self.canvas.set_cursor(cursors.RESIZE_HORIZONTAL)
            if not gtl and lmin <= x:
                self._x_click = right
            elif not ltr and x <= rmax:
                self._x_click = left
            else:
                self._x_click = x

        # 그리기 후 최초 클릭이면 좌표 수정
        if left == right:
            self._navcoordinate = (x, x)
        return

    def _on_release(self, e: MouseEvent):
        if e.inaxes is not self.ax_slider: return
        self.is_click, self.is_move = (False, False)

        if self._navcoordinate[0] == self._navcoordinate[1]:
            self._navcoordinate = (self._navcoordinate[0], self._navcoordinate[1]+self.min_distance)
        return


class BackgroundMixin(NavgatorMixin):
    def _on_draw(self, e):
        self.background = None
        self._restore_region()
        return

    def _restore_region(self, with_nav=True, empty=False, empty_with_nav=False):
        if not self.background: self._create_background()

        if empty: self.canvas.restore_region(self.background_empty)
        elif empty_with_nav: self.canvas.restore_region(self.background_empty_with_nav)
        elif with_nav: self.canvas.restore_region(self.background_with_nav)
        else: self.canvas.renderer.restore_region(self.background)
        return

    def _copy_bbox(self):
        renderer = self.canvas.renderer

        self.background_empty = renderer.copy_from_bbox(self.fig.bbox)

        self.ax_slider.xaxis.draw(renderer)
        self.ax_slider.yaxis.draw(renderer)
        self.slidercollection.draw(renderer)
        self.background_empty_with_nav = self.canvas.renderer.copy_from_bbox(self.fig.bbox)

        self._draw_artist()
        self.background = self.canvas.renderer.copy_from_bbox(self.fig.bbox)

        self.navigator.draw(self.canvas.renderer)
        self.background_with_nav = self.canvas.renderer.copy_from_bbox(self.fig.bbox)
        return

    def _draw_artist(self):
        renderer = self.canvas.renderer

        self.ax_price.xaxis.draw(renderer)
        self.ax_price.yaxis.draw(renderer)

        if self.candle_on_ma:
            self.macollection.draw(renderer)
            self.candlecollection.draw(renderer)
        else:
            self.candlecollection.draw(renderer)
            self.macollection.draw(renderer)

        self.ax_volume.xaxis.draw(renderer)
        self.ax_volume.yaxis.draw(renderer)

        self.volumecollection.draw(renderer)
        return


class DrawMixin(BackgroundMixin):
    def _set_data(self, df: pd.DataFrame, sort_df=True, calc_ma=True, change_lim=True, calc_info=True):
        super()._set_data(df, sort_df, calc_ma, change_lim, calc_info)

        # 네비게이터 높이 설정
        ysub = self._slider_ymax - self._slider_ymin
        self._ymiddle = self._slider_ymax - ysub / 2
        self.navigator.set_linewidth((ysub, 5))
        return

    def _on_release(self, e: MouseEvent):
        super()._on_release(e)
        self._set_navigator(*self._navcoordinate)

        self._restore_region(empty=True)
        self._creating_background = False
        self._create_background()
        self._restore_region()
        self._blit()
        return

    def _on_move(self, e: MouseEvent):
        self._restore_region((not self.is_click))

        self._on_move_action(e)

        if self.in_slider:
            self._change_coordinate()
            if self.is_click:
                if self.is_move: self._set_navigator(*self._navcoordinate)
                elif self.intx is not None: self._set_navigator(self._x_click, self.intx)
                self.navigator.draw(self.canvas.renderer)
            self._slider_move_action(e)
        elif self.is_click:
            self.navigator.draw(self.canvas.renderer)
        else:
            if self.in_slider or self.in_price or self.in_volume:
                self._slider_move_action(e)
            if self.in_price or self.in_volume:
                self._chart_move_action(e)

        self._blit()
        return

    def _change_coordinate(self):
        if self.intx is None: return
        x = self.intx
        left, right = self._navcoordinate

        if not self.is_click:
            lmin, lmax = (left-self._navLineWidth, left+self._navLineWidth_half)
            rmin, rmax = (right-self._navLineWidth_half, right+self._navLineWidth)
            ltel, gter = (x <= lmax, rmin <= x)
            if ltel and lmin <= x:
                self.canvas.set_cursor(cursors.RESIZE_HORIZONTAL)
            elif gter and x <= rmax:
                self.canvas.set_cursor(cursors.RESIZE_HORIZONTAL)
            elif not ltel and not gter: self.canvas.set_cursor(cursors.MOVE)
            else: self.canvas.set_cursor(cursors.POINTER)
        else:
            # 네비게이터 좌표 수정
            intx = x.__int__()
            if self.is_move:
                xsub = self._x_click - intx
                left, right = (left-xsub, right-xsub)
                self._x_click = intx
            else:
                if intx == left: left = intx
                elif intx == right: right = intx
                else:
                    if self._x_click < intx: left, right = (self._x_click, intx)
                    else: left, right = (intx, self._x_click)

            nsub = right - left
            if right < 0 or self.df.index[-1] < left or nsub < self.min_distance: left, right = self._navcoordinate
            self._navcoordinate = (left, right)
        return

    def _set_navigator(self, x1, x2):
        xmin, xmax = (x1, x2) if x1 < x2 else (x2, x1)

        left = ((self.xmin, self._ymiddle), (xmin, self._ymiddle))
        right = ((xmax, self._ymiddle), (self.xmax, self._ymiddle))
        leftline = ((xmin, self._slider_ymin), (xmin, self._slider_ymax))
        rightline = ((xmax, self._slider_ymin), (xmax, self._slider_ymax))
        self.navigator.set_segments((left, leftline, right, rightline))
        return


class LimMixin(DrawMixin):
    def _on_release(self, e: MouseEvent):
        if e.inaxes is not self.ax_slider: return
        self.is_click, self.is_move = (False, False)

        if self._navcoordinate[0] == self._navcoordinate[1]:
            self._navcoordinate = (self._navcoordinate[0], self._navcoordinate[1]+self.min_distance)
        self._set_navigator(*self._navcoordinate)
        self._lim()

        self._restore_region(empty=True)
        self._copy_bbox()
        self._restore_region()
        self._blit()
        return

    def _on_move(self, e):
        self._restore_region(with_nav=(not self.is_click), empty_with_nav=self.is_click)

        self._on_move_action(e)

        if self.in_slider:
            self._change_coordinate()
            if self.is_click:
                nsub = self._navcoordinate[1] - self._navcoordinate[0]
                if self.min_distance <= nsub: self._lim()
                if self.is_move: self._set_navigator(*self._navcoordinate)
                elif self.intx is not None: self._set_navigator(self._x_click, self.intx)
                self.navigator.draw(self.canvas.renderer)
                self._draw_blit_artist()
            self._slider_move_action(e)
        elif self.is_click:
            self.navigator.draw(self.canvas.renderer)
            self._draw_blit_artist()
        else:
            if self.in_slider or self.in_price or self.in_volume:
                self._slider_move_action(e)
            if self.in_price or self.in_volume:
                self._chart_move_action(e)

        self._blit()
        return

    def _draw_blit_artist(self):
        return self._draw_artist()

    def _lim(self):
        xmin, xmax = self._navcoordinate

        xmax += 1
        self.ax_price.set_xlim(xmin, xmax)
        self.ax_volume.set_xlim(xmin, xmax)

        indmin, indmax = (xmin, xmax)
        if xmin < 0: indmin = 0
        if indmax < 1: indmax = 1
        if indmin == indmax: indmax += 1
        ymin, ymax = (self.df[self.low][indmin:indmax].min(), self.df[self.high][indmin:indmax].max())
        ysub = (ymax - ymin) / 15
        pmin, pmax = (ymin-ysub, ymax+ysub)
        self.ax_price.set_ylim(pmin, pmax)
    
        ymax = self.df[self.volume][indmin:indmax].max()
        # self._vol_ymax = ymax*1.2
        volmax = ymax * 1.2
        self.ax_volume.set_ylim(0, volmax)

        self.set_text_coordante(xmin, xmax, pmin, pmax, volmax)
        return


class SimpleMixin(LimMixin):
    simpler = False
    limit_volume = 1_500
    default_left, default_right = (180, 10)
    _draw_blit = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 영역 이동시 주가 collection
        self.blitcandle = LineCollection([], animated=True)
        self.ax_price.add_collection(self.blitcandle)
        self.priceline = LineCollection([], animated=True, edgecolors='k')
        self.ax_price.add_artist(self.priceline)

        # 영역 이동시 거래량 collection
        self.blitvolume = LineCollection([], animated=True, edgecolors=self.colors_volume)
        self.ax_volume.add_collection(self.blitvolume)
        return

    def _set_data(self, df: pd.DataFrame, sort_df=True, calc_ma=True, change_lim=True, calc_info=True):
        super()._set_data(df, sort_df, calc_ma, False, calc_info)

        seg = self.df[['x', self.high, 'x', self.low]].values
        seg = seg.reshape(seg.shape[0], 2, 2)
        self.blitcandle.set_segments(seg)
        self.blitcandle.set_edgecolor(self.df['edgecolor'])

        pseg = self.df[['x', self.close]].values
        self.priceline.set_verts(pseg.reshape(1, *pseg.shape))

        l = self.df.__len__()
        if l < self.limit_volume:
            volseg = self.df.loc[:, ['x', 'zero', 'x', self.volume]].values
        else:
            v = self.df[['x', 'zero', 'x', self.volume]].sort_values([self.volume], axis=0, ascending=False)
            volseg = v[:self.limit_volume].values

        self.blitvolume.set_segments(volseg.reshape(volseg.shape[0], 2, 2))

        if change_lim:
            index = self.df.index[-1]
            if index < self.default_left + self.default_right: self._navcoordinate = (int(self.xmin)-1, int(self.xmax)+1)
            else: self._navcoordinate = (index-self.default_left, index+self.default_right)

        self._set_navigator(*self._navcoordinate)
        self._lim()
        return 

    def _draw_blit_artist(self):
        renderer = self.canvas.renderer

        self.ax_price.xaxis.draw(renderer)
        self.ax_price.yaxis.draw(renderer)

        if self.simpler:
            if self._draw_blit: self.priceline.draw(renderer)
            else: self.blitcandle.draw(renderer)
        elif self.candle_on_ma:
            self.macollection.draw(renderer)
            if self._draw_blit: self.blitcandle.draw(renderer)
            else: self.candlecollection.draw(renderer)
        else:
            if self._draw_blit: self.blitcandle.draw(renderer)
            else: self.candlecollection.draw(renderer)
            self.macollection.draw(renderer)

        self.ax_volume.xaxis.draw(renderer)
        self.ax_volume.yaxis.draw(renderer)

        self.blitvolume.draw(renderer)
        return


class ClickMixin(SimpleMixin):
    is_click_chart = False

    def _on_click(self, e: MouseEvent):
        if not self.is_click and e.button == MouseButton.LEFT:
            if e.inaxes is self.ax_slider: pass
            elif e.inaxes is self.ax_price or e.inaxes is self.ax_volume: return self._on_chart_click(e)
            else: return
        else: return

        self.is_click = True

        x = e.xdata.__int__()
        left, right = self._navcoordinate
        lmin, lmax = (left-self._navLineWidth, left+self._navLineWidth_half)
        rmin, rmax = (right-self._navLineWidth_half, right+self._navLineWidth)

        gtl, ltr = (lmax < x, x < rmin)
        if gtl and ltr:
            self._x_click = x
            self.is_move = True
            self.canvas.set_cursor(cursors.MOVE)
        else:
            self.canvas.set_cursor(cursors.RESIZE_HORIZONTAL)
            if not gtl and lmin <= x:
                self._x_click = right
            elif not ltr and x <= rmax:
                self._x_click = left
            else:
                self._x_click = x

        # 그리기 후 최초 클릭이면 좌표 수정
        if left == right:
            self._navcoordinate = (x, x)
        return

    def _on_release(self, e: MouseEvent):
        if not self.is_click: return
        elif e.inaxes is self.ax_slider: return super()._on_release(e)
        elif not self.in_price and not self.in_volume and not self.is_click_chart: return
        # 차트 click release action
        self.canvas.set_cursor(cursors.POINTER)
        self.is_click, self.is_move = (False, False)
        self.is_click_chart = False

        self._restore_region(empty=True)
        self._copy_bbox()
        self._restore_region()
        self._blit()
        return

    def _on_chart_click(self, e: MouseEvent):
        self.is_click = True
        self.is_click_chart = True
        self._x_click = e.x.__int__()
        self.canvas.set_cursor(cursors.RESIZE_HORIZONTAL)
        return

    def _change_coordinate(self):
        if self.is_click_chart: self._change_coordinate_chart()
        else: super()._change_coordinate()
        return

    def _change_coordinate_chart(self, e: MouseEvent):
        x = e.x.__int__()
        left, right = self._navcoordinate
        nsub = right - left
        xsub = x - self._x_click
        xdiv = (xsub / (1200 / nsub)).__int__()
        if xdiv:
            left, right = (left-xdiv, right-xdiv)
            if -1 < right and left < self.df.index[-1]:
                self._navcoordinate = (left, right)
            self._x_click = x
        return

    def _on_move(self, e):
        self._restore_region(with_nav=(not self.is_click), empty_with_nav=self.is_click)

        self._on_move_action(e)

        if self.in_slider and not self.is_click_chart:
            self._change_coordinate()
            if self.is_click:
                nsub = self._navcoordinate[1] - self._navcoordinate[0]
                if self.is_move: self._set_navigator(*self._navcoordinate)
                else:
                    self._draw_blit = 900 < nsub
                    if self.intx is not None: self._set_navigator(self._x_click, self.intx)

                if self.min_distance <= nsub: self._lim()

                self.navigator.draw(self.canvas.renderer)
                self._draw_blit_artist()
            self._slider_move_action(e)
        elif self.is_click:
            if self.is_click_chart and (self.in_price or self.in_volume):
                if (self.vmin, self.vmax) != self._navcoordinate:
                    self._change_coordinate_chart(e)
                    self._lim()
                    self._set_navigator(*self._navcoordinate)
            self.navigator.draw(self.canvas.renderer)
            self._draw_blit_artist()
        else:
            if self.in_slider or self.in_price or self.in_volume:
                self._slider_move_action(e)
            if self.in_price or self.in_volume:
                self._chart_move_action(e)

        self._blit()
        return


class SliderMixin(ClickMixin):
    pass


class Chart(SliderMixin, CM, Mixin):
    def _on_draw(self, e):
        super()._on_draw(e)
        return self.on_draw(e)

    def _on_pick(self, e):
        self.on_pick(e)
        return super()._on_pick(e)

    def _on_move(self, e):
        super()._on_move(e)
        return self.on_move(e)

    def _draw_artist(self):
        super()._draw_artist()
        return self.draw_artist()
    def _draw_blit_artist(self):
        super()._draw_blit_artist()
        return self.draw_artist()

    def _on_click(self, e):
        super()._on_click(e)
        return self.on_click(e)
    def _on_release(self, e):
        super()._on_release(e)
        return self.on_release(e)


if __name__ == '__main__':
    import json
    from time import time

    import matplotlib.pyplot as plt
    from pathlib import Path

    file = Path(__file__).parent / 'data/samsung.txt'
    # file = Path(__file__).parent / 'data/apple.txt'
    with open(file, 'r', encoding='utf-8') as txt:
        data = json.load(txt)
    data = data
    df = pd.DataFrame(data)

    t = time()
    # c = SimpleMixin()
    c = SliderMixin()
    c.set_data(df)
    t2 = time() - t
    print(f'{t2=}')
    plt.show()

