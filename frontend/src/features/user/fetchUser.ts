import axios from "axios";
import * as redux from "@reduxjs/toolkit";

import { apiUrl } from "../../shared/api";

export const fetchUserInfo = redux.createAsyncThunk(
    "auth/fetch-user-info",
    async (
        token: string,
        thunk: any,
    ) => {
        try {
            const { data } = await axios.get(
                `${ apiUrl }/users/self`, {
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": "Bearer " + token
                    }
                }
            );

            console.log(data);
            return data;
        } catch (error: unknown) {
            console.log(error);
            if (axios.isAxiosError(error)) {
                if (error.response?.status === 401) {
                    return thunk.rejectWithValue("Incorrect token");
                } else if (error.response?.status === 500) {
                    return thunk.rejectWithValue("Internal server error");
                } else if (error.code === "ERR_NETWORK") {
                    return thunk.rejectWithValue(
                        "Unable to connect to the server"
                    );
                } else {
                    return thunk.rejectWithValue(
                        "Unknown error: " + error.code
                    );
                }
            } else {
                return thunk.rejectWithValue("Unknown error: " + error);
            }
        }
    }
);