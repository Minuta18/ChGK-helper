import * as redux from "@reduxjs/toolkit";

import { Question, QuestionStatus } from "../../entities/index";

type InitialStateType = {
    questions: Array<Question>,
    is_current_question_loaded: boolean,
    is_current_answer_loaded: boolean,
    error: false,
    success: false,
}

const initialState: InitialStateType = {
    questions: [],
    is_current_answer_loaded: false,
    is_current_question_loaded: false,
    error: false,
    success: false,
};

export const questionsSlice = redux.createSlice({
    name: "questions",
    initialState,
    reducers: {

    },
    extraReducers: (builder) => {
        
    }
})
