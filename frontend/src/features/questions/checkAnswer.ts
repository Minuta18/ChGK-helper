import axios from "axios";
import * as redux from "@reduxjs/toolkit";

import { Question, QuestionStatus } from "../../entities";
import { apiUrl } from "../../shared/api";

export type checkAnswerArgs = {
    question_id: number,
    answer: string,
}

export const checkAnswer = redux.createAsyncThunk(
    "questions/check-answer",
    async (
        args: checkAnswerArgs,
        thunk: any,
    ) => {
        try {
            const response = await axios.post(
                `${ apiUrl }/answer/${ args.question_id }/check`, {
                    answer: args.answer,
                }, {
                    headers: {
                        "Content-Type": "application/json",
                    }
                }
            ); 
            
            return response.data.answer_is_correct;
        } catch (error: unknown) {
            if (axios.isAxiosError(error)) {
                if (error.response?.status == 500) {
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
)
