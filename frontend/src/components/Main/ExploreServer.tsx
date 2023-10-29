/** @format */

import {
	List,
	ListItem,
	ListItemIcon,
	ListItemText,
	Box,
	Typography,
} from "@mui/material";
import useCrud from "hooks/useCrud";
import { useEffect } from "react";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import { Link, useParams } from "react-router-dom";
import Card from "@mui/material/Card"
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Grid from "@mui/material/Grid";
import Container from "@mui/material/Container";

interface Server {
    id: number;
    name: String;
    description: string;
    icon: string;
    category_name: string;
    banner: string;
}

const ExploreServer = () => {
    const { categoryName } = useParams();
    const url = categoryName
        ? `/servers/?category_name=${categoryName}`
        : "/servers/"
    const { dataCRUD, fetchData } = useCrud<Server>([], url);

    useEffect(() => {
        fetchData();
    },[categoryName]);

    return (
        <>
            <Container maxWidth="lg">
                <Box sx={{ pt: 6 }}>
                    <Typography
                        variant="h3"
                        noWrap
                        component="h1"
                        sx={{
                            display: {
                                sm: "block",
                                fontWeight: 700,
                                letterSpacing: "-2px",
                                textTransform: "capitalize",
                            },
                            textAlign: {xs: "center", sm: "left" }
                        }}>
                        {categoryName ? categoryName : "Popular Channels"}
                    </Typography>
                </Box>
                <Box>
                    <Typography
                        variant="h6"
                        noWrap
                        component="h2"
                        color="textSecondary"
                        sx={{
                            display: {
                                sm: "block",
                                fontWeight: 700,
                                fontsize: "48px",
                                letterSpacing: "-1px",
                            },
                            textAlign: {xs: "center", sm: "left" }
                        }}>
                        {categoryName
                            ? `Channels talking about ${categoryName}`
                            : "Check out some our popular channels "}
                    </Typography>
                </Box>
                <Typography
                    variant="h6"
                    sx={{
                        pt: 6,
                        pb: 1,
                        fontWeight: 700,
                        letterSpacing: "-1px"
                    }}>
                    Recommended Channels
                </Typography>
                <Grid
                    container spacing={{ xs: 0, sm: 2 }}>
                    {dataCRUD.map((item) => (
                        <Grid item key={item.id} xs={12} sm={6} md={6} lg={3}>
                            <Card
                                sx={{
                                    height: "100%",
                                    display: "flex",
                                    flexDirection: "column",
                                    boxShadow: "none",
                                    backgroundImage: "none",    
                                }}>
                                <Link
                                    to={`/servers/${item.id}`}
                                    style={{
                                        textDecoration: "none",
                                        color: "inherit",
                                    }}>
                                    <CardMedia
                                        component="img"
                                        image={
                                            item.banner
                                                ? `${item.banner}`
                                                : "https://source.unsplash.com/randon/"
                                        }
                                        alt="random"
                                        sx={{ display: { xs: "none", sm: "block" } }} />
                                    <CardContent
                                        sx={{
                                            flexGrow: 1,
                                            p: 0,
                                            "&: last-child": {paddingBottom: 0}
                                        }}>
                                        <List>
                                            <ListItem disablePadding>
                                                <ListItemIcon
                                                    sx={{minWidth: 0}}>
                                                    <ListItemAvatar
                                                        sx={{ minWidth: "50px" }}>
                                                        <Avatar
                                                            alt="server Icon"
                                                            src={`${item.icon}`} />
                                                    </ListItemAvatar>
                                                </ListItemIcon>
                                                <ListItemText
                                                    primary={<Typography
                                                        variant="body2"
                                                        textAlign="start"
                                                        sx={{
                                                            textOverflow: "ellipsis",
                                                            overflow: "hidden",
                                                            whiteSpace: "nowrap",
                                                            fontWeight: 700,
                                                        }}>
                                                        {item.name}
                                                    </Typography>
                                                    }
                                                    secondary={<Typography variant="body2">
                                                        {item.category_name}
                                                    </Typography>
                                                    }/>
                                            </ListItem>
                                        </List>
                                    </CardContent>
                                </Link>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
            </Container>
        </>
    )
        
}

export default ExploreServer