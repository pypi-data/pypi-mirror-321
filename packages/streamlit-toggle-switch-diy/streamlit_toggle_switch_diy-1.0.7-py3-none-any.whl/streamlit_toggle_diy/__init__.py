import os
import streamlit.components.v1 as components
import streamlit as st

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_toggle_diy",
        url="http://localhost:3001",  # 本地开发时的地址
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_toggle_diy", path=build_dir)


def st_toggle_switch(
    key=None,
    label_start="",          # 前标签文字
    label_end="",            # 后标签文字
    justify='flex-start',    # 对齐方式
    default_value=False,     # 默认开关状态
    inactive_color='#D3D3D3',
    active_color="#11567f",
    track_color="#29B5E8",
    label_bg_color_start=None,
    label_bg_color_end=None,
    background_color_near_button_start=None,
    background_color_near_button_end=None,
    border_radius=None,

    # ============== 新增可选参数 ==============
    label_start_color="#7f1916",  # 前标签文字颜色
    label_end_color="#FFFFFF",    # 后标签文字颜色
    label_font_size="14px",       # 标签字体大小
    label_font_weight="bold",     # 标签字体粗细
    switch_size="medium",         # Switch 尺寸，"small" 或 "medium"
):
    """
    在 Streamlit 中创建一个可自定义颜色、大小的切换开关组件。

    Parameters
    ----------
    key: str
        组件在 session_state 中的 key，用于区分多个组件实例。
    label_start: str
        开关左侧标签文字。
    label_end: str
        开关右侧标签文字。
    justify: {'flex-start', 'center', 'flex-end'}
        标签和开关在容器中的对齐方式。
    default_value: bool
        开关的默认状态，True 为打开，False 为关闭。
    inactive_color: str
        开关未激活时的按钮颜色。
    active_color: str
        开关激活时的按钮颜色。
    track_color: str
        开关轨道（背景）的颜色。
    label_bg_color_start: str
        左 / 上方标签背景色（如果需要渐变，可与 label_bg_color_end 联合使用）。
    label_bg_color_end: str
        右 / 下方标签背景色（如果需要渐变，可与 label_bg_color_start 联合使用）。
    background_color_near_button_start: str
        开关附近背景的起始颜色（可配合 background_color_near_button_end 做渐变）。
    background_color_near_button_end: str
        开关附近背景的结束颜色（可配合 background_color_near_button_start 做渐变）。
    border_radius: str
        组件的圆角，如 '4px', '8px', '50%' 等。

    label_start_color: str
        前标签文字颜色（默认为 #7f1916）。
    label_end_color: str
        后标签文字颜色（默认为 #FFFFFF）。
    label_font_size: str
        标签文字的字体大小（如 '14px' 等）。
    label_font_weight: str
        标签文字的粗细（如 'bold', 'normal', '500' 等）。
    switch_size: {'small', 'medium'}
        切换开关本身的尺寸。

    Returns
    -------
    bool
        返回切换后的状态。如果无法获取，则返回 default_value。
    """

    toggle_value = _component_func(
        key=key,
        default_value=default_value,
        label_start=label_start,
        label_end=label_end,
        justify=justify,
        inactive_color=inactive_color,
        active_color=active_color,
        track_color=track_color,
        label_bg_color_start=label_bg_color_start,
        label_bg_color_end=label_bg_color_end,
        background_color_near_button_start=background_color_near_button_start,
        background_color_near_button_end=background_color_near_button_end,
        border_radius=border_radius,

        # === 将新增参数传给前端 ===
        label_start_color=label_start_color,
        label_end_color=label_end_color,
        label_font_size=label_font_size,
        label_font_weight=label_font_weight,
        switch_size=switch_size,
    )
    return toggle_value if toggle_value is not None else default_value


# 仅在开发环境时演示组件效果
if not _RELEASE:
    st.header('Streamlit Toggle Switch - Dev Mode')
    st.write('---')

    # 使用 color_picker 选择不同颜色
    color1_start = st.color_picker('选择 Question 1 标签起始背景颜色', '#FFD700')
    color1_end = st.color_picker('选择 Question 1 标签结束背景颜色', '#FF8C00')

    color2_start = st.color_picker('选择 Question 2 标签起始背景颜色', '#ADFF2F')
    color2_end = st.color_picker('选择 Question 2 标签结束背景颜色', '#32CD32')

    color3_start = st.color_picker('选择 Question 3 标签起始背景颜色', '#1E90FF')
    color3_end = st.color_picker('选择 Question 3 标签结束背景颜色', '#0000FF')

    color4_start = st.color_picker('选择 Question 4 标签起始背景颜色', '#FF69B4')
    color4_end = st.color_picker('选择 Question 4 标签结束背景颜色', '#FF1493')

    color5_start = st.color_picker('选择 Disable Filter 标签起始背景颜色', '#00FA9A')
    color5_end = st.color_picker('选择 Disable Filter 标签结束背景颜色', '#00FF7F')

    # 新增颜色选择器用于按钮附近的背景颜色
    button_bg_start = st.color_picker('按钮附近的起始背景颜色', '#FFFFFF')
    button_bg_end = st.color_picker('按钮附近的结束背景颜色', '#FFFFFF')

    # 新增圆角选择器
    border_radius = st.text_input('组件圆角（如：4px, 8px, 50%）', '8px')

    # 新增对齐方式选择器
    justify = st.selectbox(
        '标签与开关的对齐方式',
        ('flex-start', 'center', 'flex-end')
    )

    # 新增标签文字颜色选择
    label_start_color = st.color_picker("左侧标签文字颜色", "#7f1916")
    label_end_color = st.color_picker("右侧标签文字颜色", "#FFFFFF")

    # 标签字体大小与粗细
    label_font_size = st.text_input("标签字体大小", "14px")
    label_font_weight = st.text_input("标签字体粗细", "bold")

    # Switch 尺寸选择器
    switch_size = st.selectbox(
        "Switch 尺寸",
        ("small", "medium")
    )

    columns = st.columns(3)
    with columns[0]:
        st_toggle_switch(
            key='c1',
            label_start="Question 1",
            label_end="",  # 不显示后标签
            justify=justify,
            default_value=True,
            inactive_color='#D3D3D3',
            active_color="#11567f",
            track_color="#29B5E8",
            label_bg_color_start=color1_start,
            label_bg_color_end=color1_end,
            background_color_near_button_start=button_bg_start,
            background_color_near_button_end=button_bg_end,
            border_radius=border_radius,
            label_start_color=label_start_color,
            label_end_color=label_end_color,
            label_font_size=label_font_size,
            label_font_weight=label_font_weight,
            switch_size=switch_size,
        )

        st_toggle_switch(
            key="input_toggle",
            label_start="",
            label_end="Question 2",
            justify='flex-start',
            default_value=True,
            inactive_color='#95e1d3',
            active_color="#f38181",
            track_color="#f38181",
            label_bg_color_start='white',
            label_bg_color_end='black',
            background_color_near_button_start='blue',
            background_color_near_button_end='black',
            border_radius='10px',
            label_start_color="#000000",
            label_end_color="#FFFFFF",
            label_font_size="12px",
            label_font_weight="normal",
            switch_size="small",
        )

    with columns[1]:
        st_toggle_switch(
            key='q2',
            label_start="",  # 不显示前标签
            label_end="Question 3",
            justify=justify,
            default_value=True,
            inactive_color='#DDA0DD',
            active_color="#9400D3",
            track_color="#BA55D3",
            label_bg_color_start=color3_start,
            label_bg_color_end=color3_end,
            background_color_near_button_start=button_bg_start,
            background_color_near_button_end=button_bg_end,
            border_radius=border_radius,
            label_start_color=label_start_color,
            label_end_color=label_end_color,
            label_font_size=label_font_size,
            label_font_weight=label_font_weight,
            switch_size=switch_size,
        )
        st_toggle_switch(
            key='q3',
            label_start="",  # 不显示前标签
            label_end="Question 4",
            justify=justify,
            default_value=False,
            inactive_color='#FFA07A',
            active_color="#FF4500",
            track_color="#FF6347",
            label_bg_color_start=color4_start,
            label_bg_color_end=color4_end,
            background_color_near_button_start=button_bg_start,
            background_color_near_button_end=button_bg_end,
            border_radius=border_radius,
            label_start_color=label_start_color,
            label_end_color=label_end_color,
            label_font_size=label_font_size,
            label_font_weight=label_font_weight,
            switch_size=switch_size,
        )

    with columns[2]:
        st_toggle_switch(
            key='q1',
            label_start="Disable Filter",
            label_end="",  # 不显示后标签
            justify=justify,
            default_value=True,
            inactive_color='#98FB98',
            active_color="#00FF7F",
            track_color="#00FA9A",
            label_bg_color_start=color5_start,
            label_bg_color_end=color5_end,
            background_color_near_button_start=button_bg_start,
            background_color_near_button_end=button_bg_end,
            border_radius=border_radius,
            label_start_color=label_start_color,
            label_end_color=label_end_color,
            label_font_size=label_font_size,
            label_font_weight=label_font_weight,
            switch_size=switch_size,
        )
        range_slider_toggle = st_toggle_switch(
            key='ql',
            label_start="Disable Filter",
            label_end="",  # 不显示后标签
            justify=justify,
            default_value=True,
            inactive_color='#98FB98',
            active_color="#00FF7F",
            track_color="#00FA9A",
            label_bg_color_start=color5_start,
            label_bg_color_end=color5_end,
            background_color_near_button_start=button_bg_start,
            background_color_near_button_end=button_bg_end,
            border_radius=border_radius,
            label_start_color=label_start_color,
            label_end_color=label_end_color,
            label_font_size=label_font_size,
            label_font_weight=label_font_weight,
            switch_size=switch_size,
        )
        range_slider = st.slider(
            label="Filter Range",
            min_value=0,
            max_value=100,
            disabled=range_slider_toggle,
        )
