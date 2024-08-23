import axios from "axios";
import * as redux from "@reduxjs/toolkit";

import { apiUrl } from "../../shared/api";

export interface UserInfo {
    user_id: number;
    token: string;
}

export const fetchUserSettings = redux.createAsyncThunk(
    "auth/fetch-user-settings",
    async (
        info: UserInfo,
        thunk: any,
    ) => {
        try {
            const response = await axios.get(
                `${apiUrl}/users/settings/${info.user_id}`, {
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": "Bearer " + info.token
                    }
                }
            );

            return response.data.user;
        } catch (error: unknown) {
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
