import random
from typing import List, Tuple, Literal, Any, Union

from spiderpy3.utils.verify.sdk.cBezier import bezierTrajectory
from spiderpy3.utils.execute.js import execute_js_code_by_execjs

SlidePoint = Tuple[int, int]
SlideMode = Literal["bezier_curve", "ghost_cursor"]
TimeInterval = Union[int, float, Tuple[int, int], Tuple[float, float]]
SlideTrajectory = Union[Tuple[int, int, int], Tuple[int, int, float]]


class Slide(object):
    @classmethod
    def get_slide_points_by_bezier_curve(
            cls,
            distance: int,
            numberList=random.randint(25, 45),  # noqa
            le=4,
            deviation=10,
            bias=0.5,
            type=2,  # noqa
            cbb=1,
            yhh=5
    ) -> List[SlidePoint]:
        """

        :param distance:
        :param numberList: 返回的数组的轨迹点的数量 numberList = 150
        :param le: 几阶贝塞尔曲线，越大越复杂 如 le = 4
        :param deviation: 轨迹上下波动的范围 如 deviation = 10
        :param bias: 波动范围的分布位置 如 bias = 0.5
        :param type: 0表示均速滑动，1表示先慢后快，2表示先快后慢，3表示先慢中间快后慢 如 type = 1
        :param cbb: 在终点来回摆动的次数
        :param yhh: 在终点来回摆动的范围
        :return:
        """
        bt = bezierTrajectory()
        result = bt.trackArray([0, 0], [distance, 0],
                               numberList, le=le, deviation=deviation, bias=bias, type=type, cbb=cbb, yhh=yhh)
        result = result["trackArray"].tolist()
        slide_points = [(round(i[0]), round(i[1])) for i in result]
        return slide_points

    @classmethod
    def get_slide_points_by_ghost_cursor(cls, distance: int, **_kwargs: Any) -> List[SlidePoint]:
        js_code = '''function sdk(from,to){const{path}=require("ghost-cursor");return path(from,to,{useTimestamps:false})}'''  # noqa
        result = execute_js_code_by_execjs(js_code=js_code, func_name="sdk",
                                           func_args=({"x": 0, "y": 0}, {"x": distance, "y": 0}))
        slide_points = [(round(i["x"]), round(i["y"])) for i in result]
        return slide_points

    @classmethod
    def get_slide_points(
            cls,
            distance: int,
            slide_mode: SlideMode = "bezier_curve",
            **kwargs: Any
    ) -> List[SlidePoint]:
        if slide_mode == "bezier_curve":
            slide_points = cls.get_slide_points_by_bezier_curve(distance, **kwargs)
        elif slide_mode == "ghost_cursor":
            slide_points = cls.get_slide_points_by_ghost_cursor(distance, **kwargs)
        else:
            raise ValueError(f"不支持的 slide_mode：{slide_mode}！")
        return slide_points

    @classmethod
    def get_slide_trajectories(
            cls,
            slide_points: List[SlidePoint],
            time_interval: TimeInterval = (5, 10),
            use_offset: bool = False
    ) -> List[SlideTrajectory]:
        slide_trajectories = []

        def get_trajectory(x, y):
            if isinstance(time_interval, int) or isinstance(time_interval, float):
                trajectory = (x, y, time_interval)
            else:
                if isinstance(time_interval, tuple) and len(time_interval) == 2:
                    if all(map(lambda _: isinstance(_, int), time_interval)):
                        trajectory = (x, y, random.randint(*time_interval))
                    elif all(map(lambda _: isinstance(_, float), time_interval)):
                        trajectory = (x, y, random.uniform(*time_interval))
                    else:
                        raise ValueError(f"不支持的 time_interval：{time_interval}！")
                else:
                    raise ValueError(f"不支持的 time_interval：{time_interval}！")
            return trajectory

        def core():
            if use_offset:
                current_x, current_y = 0, 0
                for slide_point in slide_points:
                    x, y = slide_point
                    offset_x, offset_y = x - current_x, y - current_y
                    trajectory = get_trajectory(offset_x, offset_y)
                    slide_trajectories.append(trajectory)
                    current_x, current_y = x, y
            else:
                for slide_point in slide_points:
                    x, y = slide_point
                    trajectory = get_trajectory(x, y)
                    slide_trajectories.append(trajectory)

        core()

        return slide_trajectories


if __name__ == '__main__':
    print(Slide.get_slide_points_by_bezier_curve(121))
    print(Slide.get_slide_points_by_ghost_cursor(121))
    print(Slide.get_slide_points(121))
    print(Slide.get_slide_trajectories(
        Slide.get_slide_points(121)
    ))
    print(Slide.get_slide_trajectories(
        Slide.get_slide_points(121),
        time_interval=.02
    ))
