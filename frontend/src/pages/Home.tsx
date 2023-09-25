import React from "react";
import { Box, CssBaseline } from "@mui/material"
import PrimaryAppBar from "pages/templates/PrimaryAppBar";
import PrimaryDraw from "pages/templates/PrimaryAppBar";
import SecondaryDraw from "pages/templates/SecondaryDraw";
import Main from "pages/templates/Main";

const Home = () => {
    return(
        <Box sx={{ display: "flex" }}>
            <CssBaseline />
            <PrimaryAppBar />
            <PrimaryDraw />
            <SecondaryDraw />
            <Main />
        </Box>
    );
};
export default Home