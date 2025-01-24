import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib";
import React, { useEffect, useRef } from "react";
import { createTheme } from "@material-ui/core/styles";
import { Typography, Switch, Grid } from "@material-ui/core";
import { ThemeProvider } from "@material-ui/styles";

interface ToggleSwitchProps {
  // 原有参数
  default_value: boolean;
  label_start?: string;
  label_end?: string;
  justify?: "flex-start" | "center" | "flex-end";
  active_color?: string;
  inactive_color?: string;
  track_color?: string;
  label_bg_color_start?: string;
  label_bg_color_end?: string;
  background_color_near_button_start?: string;
  background_color_near_button_end?: string;
  border_radius?: string;
  label_start_color?: string; // 左侧标签文字颜色
  label_end_color?: string;   // 右侧标签文字颜色
  label_font_size?: string;   // 标签文字大小
  label_font_weight?: string; // 标签文字粗细
  switch_size?: "small" | "medium"; // Switch 尺寸
}

const StreamlitToggle = (props: ComponentProps) => {
  // 1. 从 props.args 中解构所有参数
  const {
    // -- 基础必选 --
    default_value,
    // -- 已有可选 --
    label_start,
    label_end,
    justify = "flex-start",
    inactive_color='#CEE8FF',
    active_color="#00668c",
    track_color="#3D5A80",
    label_bg_color_start="#FFFFFF",
    label_bg_color_end="yellow",
    background_color_near_button_start="#FFFFFF",
    background_color_near_button_end="#FFFFFF",
    border_radius='30px',
    label_start_color="#333333",
    label_end_color="red",
    label_font_size="16px",
    label_font_weight="bold",
    switch_size="medium",
  } = props.args as ToggleSwitchProps;

  // 2. 引入容器引用，以便 setFrameHeight() 时保证内容高度正确
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // 通知 Streamlit 调整 iframe 高度
    Streamlit.setFrameHeight();
  }, []);

  // 3. 管理 Switch 状态
  const [state, setState] = React.useState({
    checkStatus: default_value,
  });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setState({ ...state, [event.target.name]: event.target.checked });
    // 将选中状态传回 Python
    Streamlit.setComponentValue(event.target.checked);
  };

  // 4. Material-UI 主题：动态覆盖 Switch 的颜色
  const snowflakeTheme = createTheme({
    overrides: {
      MuiSwitch: {
        switchBase: {
          color: inactive_color, // 未选中时的按钮颜色
        },
        colorSecondary: {
          "&$checked": {
            color: active_color, // 选中时按钮颜色
          },
        },
        track: {
          opacity: 0.1,
          backgroundColor: track_color, // 轨道颜色
          "$checked$checked + &": {
            opacity: 1,
            backgroundColor: track_color,
          },
        },
      },
    },
  });

  // 5. 样式：标签与背景
  const labelStartStyle: React.CSSProperties = {
    backgroundColor: label_bg_color_start,
    color: label_start_color,
    padding: "4px 8px",
    borderRadius: border_radius,
    display: "inline-block",
    fontWeight: label_font_weight,
    fontSize: label_font_size,
  };

  const labelEndStyle: React.CSSProperties = {
    backgroundColor: label_bg_color_end,
    color: label_end_color,
    padding: "4px 8px",
    borderRadius: border_radius,
    display: "inline-block",
    fontWeight: label_font_weight,
    fontSize: label_font_size,
  };

  // 背景（左右渐变或单色）
  const buttonBackgroundStyle: React.CSSProperties = {
    background:
      background_color_near_button_start && background_color_near_button_end
        ? `linear-gradient(to right, ${background_color_near_button_start}, ${background_color_near_button_end})`
        : background_color_near_button_start ||
          background_color_near_button_end ||
          "#ffffff",
    padding: "10px",
    borderRadius: border_radius,
    display: "flex",
    alignItems: "center",
  };

  // 6. 组件 JSX
  return (
    <ThemeProvider theme={snowflakeTheme}>
      <Typography
        component="div"
        variant="subtitle1"
        paragraph={false}
        gutterBottom={false}
      >
        <div ref={containerRef} style={buttonBackgroundStyle}>
          <Grid container justifyContent={justify} alignItems="center" spacing={1}>
            {label_start && (
              <Grid item>
                <span style={labelStartStyle}>{label_start}</span>
              </Grid>
            )}
            <Grid item>
              <Switch
                checked={state.checkStatus}
                onChange={handleChange}
                name="checkStatus"
                size={switch_size} // 新增：Switch 尺寸
              />
            </Grid>
            {label_end && (
              <Grid item>
                <span style={labelEndStyle}>{label_end}</span>
              </Grid>
            )}
          </Grid>
        </div>
      </Typography>
    </ThemeProvider>
  );
};

export default withStreamlitConnection(StreamlitToggle);
