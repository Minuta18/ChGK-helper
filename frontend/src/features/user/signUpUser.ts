import axios from "axios";
import * as redux from '@reduxjs/toolkit';

import { apiUrl } from "../../shared/api";

export type SignUpFormValues = {
    username: string,
    email: string,
    password: string,
}

export const signUpUser = redux.createAsyncThunk(
    "auth/sign-in",
    async (
        formValues: SignUpFormValues, 
        thunk: any,
    ) => {
        try {
            const { data } = await axios.post(`${apiUrl}/users/`, {
                "nickname": formValues.username,
                "email": formValues.email,
                "password": formValues.password,
            }, {
                headers: {
                    "Content-Type": "application/json"
                }
            })

            return data;
        } catch (error: unknown) {
            if (axios.isAxiosError(error)) {
                console.log(error);
                if (error.response?.status === 400) {
                    const message = error.response?.data?.message;
                    return thunk.rejectWithValue(message); 
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
