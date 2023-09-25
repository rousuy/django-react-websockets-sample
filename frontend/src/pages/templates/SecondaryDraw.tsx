/** @format */

import { Box, Typography } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import React from "react";
import AxiosInstance from "../../axios";
import useAxiosWithInterceptor from "../../axios";
import axios from "axios";


axios().get("/servers/?category_name=category_1").then(response => {
	console.log(response.data);
}).catch((error) => {console.log(error)});

const SecondaryDraw = () => {
	const theme = useTheme();
	return (
		<Box
			sx={{
				minWidth: `${theme.secondaryDraw.width}px`,
				height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
				mt: `${theme.primaryAppBar.height}px`,
				borderRight: `1px solid ${theme.palette.divider}`,
				display: { xs: "none", sm: "block" },
				overflow: "auto",
			}}>
			{[...Array(100)].map((_, i) => (
				<Typography key={i} paragraph>
					{i + 1}
				</Typography>
			))}
		</Box>
	);
};
export default SecondaryDraw;
