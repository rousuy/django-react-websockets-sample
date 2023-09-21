/** @format */

import {
	AppBar,
	Box,
	Drawer,
	IconButton,
	Toolbar,
	Typography,
	useMediaQuery,
} from "@mui/material";
import { useTheme } from "@mui/material/styles";
import { Link } from "react-router-dom";
import MenuIcon from "@mui/icons-material/Menu";
import { useState, useEffect } from "react";
import React from "react";

const PrimaryAppBar = () => {
	const theme = useTheme();
	const isSmallScreen = useMediaQuery(theme.breakpoints.up("sm"));
	const [sideMenu, setSideMenu] = useState(!isSmallScreen);
	

	useEffect(() => {
		if (isSmallScreen && sideMenu) {
			setSideMenu(!isSmallScreen);
		}
	}, [isSmallScreen, sideMenu]);

	const toggleDrawer =
		(open: boolean) => (event: React.KeyboardEvent | React.MouseEvent) => {
			if (
				event.type === "keydown" &&
				((event as React.KeyboardEvent).key === "Tab" ||
					(event as React.KeyboardEvent).key === "Shift")
			) {
				return;
			}
			setSideMenu(open);
		};

	return (
		<AppBar
			sx={{
				zIndex: theme => theme.zIndex.drawer + 2,
				backgroundColor: theme.palette.background.default,
				borderBottom: `1px solid ${theme.palette.divider}`,
			}}>
			<Toolbar
				variant="dense"
				sx={{
					height: theme.primaryAppBar.height,
					minHeight: theme.primaryAppBar.height,
				}}>
				<Box sx={{ display: { xs: "block", sm: "none" } }}>
					<IconButton
						color="inherit"
						aria-label="open drawer"
						edge="start"
						onClick={toggleDrawer(!sideMenu)}
						sx={{ mr: 2 }}>
						<MenuIcon />
					</IconButton>
				</Box>

				<Drawer anchor="left" open={sideMenu} onClose={toggleDrawer(false)}>
					{[...Array(100)].map((_, i) => (
						<Typography key={i} paragraph>
							{i + 1}
						</Typography>
					))}
				</Drawer>

				<Link to="/" style={{ textDecoration: "none", color: "inherit" }}>
					<Typography
						variant="h6"
						noWrap
						component="div"
						sx={{ display: { fontWeight: 700, letterSpacing: "-0.5px" } }}>
						DJMEET
					</Typography>
				</Link>
			</Toolbar>
		</AppBar>
	);
};

export default PrimaryAppBar;
