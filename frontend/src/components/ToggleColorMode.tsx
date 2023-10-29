/** @format */

import { CssBaseline, useMediaQuery, ThemeProvider } from "@mui/material";
import { useEffect, useState, useMemo } from "react";
import React from "react";
import createMuiTheme from "themes/theme";
import { ColorModeContext } from "context/DarkModeContext";
import Cookies from "js-cookie";

interface ToggleColorModeProps {
	children: React.ReactNode;
}

interface ToggleColorModeProps {
	children: React.ReactNode;
}

const ToggleColorMode: React.FC<ToggleColorModeProps> = ({ children }) => {
	const storedMode = Cookies.get("colorMode") as "light" | "dark";
	const preferredDarkMode = useMediaQuery("([prefers-color-scheme: dark])");
	const defaultMode = storedMode || (preferredDarkMode ? "dark" : "light");

	const [mode, setMode] = useState<"light" | "dark">(defaultMode);
	
	const toggleColorMode = React.useCallback(() => {
		setMode(prevMode => (prevMode === "light" ? "dark" : "light"));
	}, []);

	useEffect(() => {
		Cookies.set("colorMode", mode);
	}, [mode]);

	const colorMode = useMemo(() => ({ toggleColorMode }), [toggleColorMode]);

	const theme = useMemo(() => createMuiTheme(mode || "light"), [mode]);

	return (
		<ColorModeContext.Provider value={colorMode}>
			<ThemeProvider theme={theme}>
				<CssBaseline />
				{children}
			</ThemeProvider>
		</ColorModeContext.Provider>
	);
};

export default ToggleColorMode;
