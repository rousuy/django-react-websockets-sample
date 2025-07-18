/** @format */

import { Box } from "@mui/material";
import { ReactNode } from "react";
import { useTheme } from "@mui/material/styles";

type Props = {
	children: ReactNode;
}

const Main: React.FC<Props> = ({ children }) => {
	const theme = useTheme();
	return (
		<Box
			sx={{
				flexGrow: 1,
				mt: `${theme.primaryAppBar.height}px`,
				height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
				overflow: "hidden",
			}}>
			{children}
		</Box>
	);
};
export default Main;
