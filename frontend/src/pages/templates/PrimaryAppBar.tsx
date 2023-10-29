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
import ExploreCategories from "components/SecondaryDraw/ExploreCategories";
import AccountButton from "components/PrimaryAppBar/AccountButton";

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
	
	const list = () => (
		<Box sx={{
			paddingBottom: theme.primaryAppBar.height,
			minWidth: 200,
			}}
			role="presentation"
			onClick={toggleDrawer(false)}
			onKeyDown={toggleDrawer(false)}>
			<ExploreCategories />
		</Box>
	);

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
					{list()}
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
				<Box sx={{ flexGrow: 1 }}></Box>
				<AccountButton />
			</Toolbar>
		</AppBar>
	);
};

export default PrimaryAppBar;
