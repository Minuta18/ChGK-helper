import * as redux from "@reduxjs/toolkit";

import * as Features from "../../features/index";
import { Question, QuestionStatus } from "../../entities/index";

type InitialStateType = {
    questions: Array<Question>,
    is_current_question_loaded: boolean,
    is_current_answer_loaded: boolean,
    is_current_question_answered: boolean,
    is_current_question_fetch_started: boolean,
    last_question_id: number;
    error: boolean|any,
    success: boolean,
}

const initialState: InitialStateType = {
    questions: [],
    is_current_answer_loaded: false,
    is_current_question_loaded: false,
    is_current_question_answered: false,
    is_current_question_fetch_started: false,
    last_question_id: 0,
    error: false,
    success: false,
};

export const questionsSlice = redux.createSlice({
    name: "questions",
    initialState,
    reducers: {

    },
    extraReducers: (builder) => {
        builder
            .addCase(Features.fetchRandomQuestion.pending, (state) => {
                state.is_current_question_loaded = false;
                state.error = false;
                state.success = false;
                state.is_current_question_fetch_started = true;
            }) 
            .addCase(Features.fetchRandomQuestion.fulfilled, 
            (state, action) => {
                state.is_current_question_loaded = true;
                state.error = false;
                state.success = true;
                state.last_question_id = 
                    state.questions.push(action.payload) - 1;
            })
            .addCase(Features.fetchRandomQuestion.rejected, 
            (state, action) => {
                state.is_current_question_loaded = true;
                state.error = action.payload;
                state.success = false;
            })
    }
})
