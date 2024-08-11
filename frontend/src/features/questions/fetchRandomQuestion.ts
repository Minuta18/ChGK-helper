import axios from "axios";
import * as redux from "@reduxjs/toolkit";

import { apiUrl } from "../../shared/api";

export const fetchRandomQuestion = redux.createAsyncThunk(
    "questions/fetch-random-question",
    async (
        thunk: any
    ) => {
        try {
            const { data } = await axios.get(
                `${ apiUrl }/questions/random`, {
                    headers: {
                        "Content-Type": "application/json",
                    }
                }
            ); 
        } catch (error: unknown) {

        }
    }
)
