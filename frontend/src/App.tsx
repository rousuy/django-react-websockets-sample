import React from "react";
import Home from "./pages/Home";
import createMuiTheme from "./themes/theme";
import {
    Route,
    RouterProvider,
    createBrowserRouter,
    createRoutesFromElements,
} from "react-router-dom";
import { ThemeProvider } from "@emotion/react";


const router = createBrowserRouter(
    createRoutesFromElements(
        <Route>
            <Route path="/" element={<Home />} />
        </Route>
    )
);

const App = () => {
    const theme = createMuiTheme();
    return (
        <ThemeProvider theme={theme}>
            <RouterProvider router={router} />
        </ThemeProvider>
    );
};

export default App;