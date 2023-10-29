import { AccountCircle, Brightness4 } from "@mui/icons-material";
import { IconButton, Menu, MenuItem } from "@mui/material";
import Box from "@mui/material/Box";
import DarkModeSwitch from "./DarkMode/DarkModeSwitch";
import React, { useState } from "react";




const AccountButton = () => {
    const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

    const isMenuOpen = Boolean(anchorEl);

    const handleProfileMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
        setAnchorEl(event.currentTarget);
    };

    const handleMenuClose = () => {
        setAnchorEl(null);
    };

    const renderMenu = (
        <Menu
            anchorEl={anchorEl}
            anchorOrigin={{ vertical: "bottom", horizontal: "right" }}
            open={isMenuOpen}
            keepMounted
            onClose={handleMenuClose}>
            <MenuItem>
                <DarkModeSwitch />
            </MenuItem>
        </Menu>
    )
    return (
        <Box sx={{ display: { xs: "flex" } }}>
            <IconButton
                edge="end"
                color="inherit"
                onClick={handleProfileMenuOpen}>
                <AccountCircle />
            </IconButton>
            {renderMenu}
        </Box>
    );
};
export default AccountButton