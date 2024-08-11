import axios from "axios";
import * as redux from "@reduxjs/toolkit";

import { Question, QuestionStatus } from "../../entities";
import { apiUrl } from "../../shared/api";

type FetchQuestionArgs = {

}

function sleep(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

export const fetchRandomQuestion = redux.createAsyncThunk(
    "questions/fetch-random-question",
    async (
        args: FetchQuestionArgs,
        thunk: any,
    ) => {
        try {
            // await sleep(10000);

            const ques: Question = {};
            const response = await axios.get(
                `${ apiUrl }/questions/random`, {
                    headers: {
                        "Content-Type": "application/json",
                    }
                }
            ); 
            ques.text = response.data.text;
            ques.comment = response.data.comment;
            ques.id = response.data.id;
            const response2 = await axios.get(
                `${ apiUrl }/answer/get/${ ques.id }`, {
                    headers: {
                        "Content-Type": "application/json",
                    }
                }
            );
            ques.correct_answer = response2.data.correct_answer;
            ques.status = QuestionStatus.IN_PROGRESS;
            return ques;
        } catch (error: unknown) {
            if (axios.isAxiosError(error)) {
                if (error.response?.status == 404) {
                    return thunk.rejectWithValue("No questions");
                } else if (error.response?.status == 500) {
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
