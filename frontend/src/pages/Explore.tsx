import React from "react";
import { Box, CssBaseline } from "@mui/material"
import PrimaryDraw from "pages/templates/PrimaryDraw";
import PrimaryAppBar from "pages/templates/PrimaryAppBar";
import SecondaryDraw from "pages/templates/SecondaryDraw";
import Main from "pages/templates/Main";
import PopularChannels from "components/PrimaryDraw/PopularChannels";
import ExploreCategories from "components/SecondaryDraw/ExploreCategories";
import ExploreServer from "components/Main/ExploreServer";


const Home = () => {
    return(
        <Box sx={{ display: "flex" }}>
            <CssBaseline />
            <PrimaryAppBar />
            <PrimaryDraw>
                <PopularChannels open={false}/>
            </PrimaryDraw>
            <SecondaryDraw>
                <ExploreCategories />
            </SecondaryDraw>
            <Main>
                <ExploreServer />
            </Main>
        </Box>
    );
};
export default Home