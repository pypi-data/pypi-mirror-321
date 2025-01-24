from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
def run():
    class Walker(Entity):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.model = 'cube'  # 使用立方体作为行走的对象
            self.color = color.white
            self.scale = (0.5, 2, 0.5)  # 调整立方体的大小以适应行走效果
            self.speed = 2  # 行走速度
            self.position = Vec3(0, 0.5, -3)  # 初始位置稍微离开地面并向后移动一些

    app = Ursina()

    # 添加一个地面
    ground = Entity(model='plane', scale=(10, 1, 10), color=color.gray, collider='box')

    # 添加行走者
    walker = Walker()

    # 可选：添加一个第一人称控制器来自由查看场景（不是必需的，但有助于观察效果）
    player = FirstPersonController()

    # 运行应用
    app.run()