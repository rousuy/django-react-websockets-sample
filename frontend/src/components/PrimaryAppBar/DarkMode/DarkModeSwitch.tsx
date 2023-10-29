import { useContext } from "react";
import { useTheme } from "@mui/material/styles";
import { ColorModeContext } from "context/DarkModeContext";
import { IconButton, Typography } from "@mui/material";
import  ToggleOffIcon  from "@mui/icons-material/ToggleOff";
import ToggleOnIcon from "@mui/icons-material/ToggleOn";

const DarkModeSwitch = () => {
    const theme = useTheme();
    const colorMode = useContext(ColorModeContext);
    return (
        <>
            <Typography variant="body2" sx={{ textTransform: "capitalize" }}>
                {theme.palette.mode} mode
            </Typography>
            <IconButton
                sx={{ m: 0, p: 0, pl: 2 }}
                onClick={colorMode.toggleColorMode}
                color="inherit">
                {theme.palette.mode === "dark" ? (
                    <ToggleOffIcon sx={{ fontSize: "2.5rem", p: 0 }} />
                ) : (
                    <ToggleOnIcon sx={{ fontSize: "2.5rem"}} />
                )}
            </IconButton>
        </>
    );
};
export default DarkModeSwitch;