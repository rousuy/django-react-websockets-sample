import React from "react";
import Home from "pages/Home";
import createMuiTheme from "themes/theme";
import {
    Route,
    RouterProvider,
    createBrowserRouter,
    createRoutesFromElements,
} from "react-router-dom";
import { ThemeProvider } from "@emotion/react";
import Explore from "pages/Explore"
import ToggleColorMode from "components/ToggleColorMode";


const router = createBrowserRouter(
    createRoutesFromElements(
        <Route>
            <Route path="/" element={<Home />} />
            <Route path="/explore/:categoryName" element={<Explore />} />
        </Route>
    )
);

const App = () => {
    return (
        <ToggleColorMode>
            <RouterProvider router={router} />
        </ToggleColorMode>    
    );
};

export default App;