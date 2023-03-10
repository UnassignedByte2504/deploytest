import React from "react";
import { useState, useContext } from "react";
import { Context } from "../../../store/appContext.js";
import { Link, useParams, Navigate, useNavigate } from "react-router-dom";
import ArrowForwardIcon from "@mui/icons-material/ArrowForward";
import Button from "@mui/material/Button";
import { Box, Divider, Typography, useTheme } from "@mui/material";
import Follows from "../aux/Follows.jsx";
import FlexEvenly from "../../styledcomponents/FlexEvenly.jsx";
import { followUser, unfollowUser } from "../../../api calls/follows.js";

const FollowButtons = () => {
  const params = useParams();
  const { store, actions } = useContext(Context);
  const username = params.username;
  const currentUser = sessionStorage.getItem("current_user");
  const [followText, setFollowText] = useState("Seguir");
  const [trigger, setTrigger] = useState();
  const theme = useTheme();
  const followersList = sessionStorage.getItem("followers_list");

  const follow = async (username) => {
    await followUser(username);
    actions.setReRender();
  };

  const unFollow = async (username) => {
    await unfollowUser(username);
    window.location.reload;
    actions.setReRender();
  };

  return (
    <>
      {username == currentUser ? null : (
        <Box
          sx={{
            display: "flex",
            flexDirection: "row",
            justifyContent: "center",
            marginTop: "0.5rem",
          }}
        >
          {followersList.includes(currentUser) ? (
            <Button
              variant="contained"
              sx={{
                color: "white",
                fontWeight: "700",
                backgroundColor: "#de3332",
                textTransform: "none",
                width:"8rem",
                paddingLeft:"0",
                paddingRight:"0"
              }}
              onClick={() => unFollow(username)}
            >
              Dejar de seguir
            </Button>
          ) : (
            <Button
              variant="contained"
              sx={{
                color: "white",
                fontWeight: "700",
                backgroundColor: "#fa7d3f",
                textTransform: "none",
              }}
              onClick={() => follow(username)}
            >
              Seguir
            </Button>
          )}
        </Box>
      )}
    </>
  );
};

export default FollowButtons;
