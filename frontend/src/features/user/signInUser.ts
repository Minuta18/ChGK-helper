import axios from "axios";
import * as redux from '@reduxjs/toolkit';

import { apiUrl } from "../../shared/api";

export type LoginFormValues = {
    username: string, 
    password: string,
}

export const signInUser = redux.createAsyncThunk(
    "auth/sign-in",
    async (
        formValues: LoginFormValues, 
        thunk: any,
    ) => {
        try {
            const response = await axios.post(`${apiUrl}/auth/login`, {
                "nickname": formValues.username,
                "password": formValues.password,
            }, {
                headers: {
                    "Content-Type": "application/json"
                }
            })

            return response.data.token;
        } catch (error: unknown) {
            if (axios.isAxiosError(error)) {
                console.log(error);
                if (error.response?.status === 401) {
                    return thunk.rejectWithValue("Incorrect password");
                } else if (error.response?.status === 404) {
                    return thunk.rejectWithValue("Could not find user");
                } else if (error.response?.status === 500) {
                    return thunk.rejectWithValue("Internal server error");
                } else if (error.code === "ERR_NETWORK") {
                    return thunk.rejectWithValue(
                        "Unable to connect to the server"
                    );
                }
            } else {
                return thunk.rejectWithValue("Unknown error: " + error);
            }
        }
    }
);

