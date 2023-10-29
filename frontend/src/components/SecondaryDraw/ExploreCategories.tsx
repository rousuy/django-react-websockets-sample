/** @format */

import {
	List,
	ListItem,
	ListItemButton,
	ListItemIcon,
	ListItemText,
	Box,
	Typography,
} from "@mui/material";
import useCrud from "hooks/useCrud";
import { useEffect } from "react";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import { Link } from "react-router-dom";
import { useTheme } from "@mui/material/styles";

interface Category {
    id: number;
    name: string;
    description: string;
    icon: string;
}


const ExploreCategories = () => {
    const theme = useTheme();
    const isDarkMode = theme.palette.mode === "dark";
    const { dataCRUD, error, isLoading, fetchData } = useCrud<Category>(
        [],
        "/servers/categories/"
    )
    useEffect(() => {
        fetchData();
    }, []);

    return <>
        <Box sx={{
            px: 2,
            height: "50px",
            display: "flex",
            alignItems: "center",
            borderBottom: `1px solid ${theme.palette.divider}`,
            position: "sticky",
            top: 0,
            backgroundColor: theme.palette.background.default
        }}>
            Explore
        </Box>
        <List sx={{ py: 0 }}>
            {dataCRUD.map((item) => (
                <ListItem
                    disablePadding
                    key={item.id}
                    sx={{ display: "block" }}
                    dense={true}>
                    <Link
                        to={`/explore/${item.name}`}
                        style={{ textDecoration: "none", color: "inherit" }}>
                        <ListItemButton
                            sx={{ minHeight: 48 }}>
                            <ListItemIcon sx={{
                                minWidth: 0,
                                justifyContent: "center",
                            }}>
                                <ListItemAvatar
                                sx={{ minWidth: "0px" }}>
                                <Avatar
                                    alt="Category Icon"
                                    src={`${item.icon}`}
                                    style={{
                                        width: "25px",
                                        height: "25px",
                                        display: "flex",
                                        margin: "auto",
                                        fontSize: "12px",
                                        filter: isDarkMode ? "invert(100%)" : "none",
                                    }}/>
                                </ListItemAvatar>
                            </ListItemIcon>
                            <ListItemText
                                primary={
                                    <Typography
                                        variant="body1"
                                        textAlign="start"
                                        paddingLeft={1}>
                                        {item.name}
                                    </Typography>} />
                        </ListItemButton>
                    </Link>
                </ListItem>
            ))}

        </List>
    </>
};

export default ExploreCategories