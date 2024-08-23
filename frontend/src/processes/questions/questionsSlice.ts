import * as redux from "@reduxjs/toolkit";

import * as Features from "../../features/index";
import { Question, QuestionStatus } from "../../entities/index";

type InitialStateType = {
    questions: Array<Question>,
    is_current_question_loaded: boolean,
    is_current_answer_loaded: boolean,
    is_current_question_fetch_started: boolean,
    is_current_answer_fetch_started: boolean,
    checking_result: any,
    last_question_id: number;
    error: boolean|any,
    success: boolean,
    selected_question: number|null,
}

const initialState: InitialStateType = {
    questions: [],
    is_current_answer_loaded: false,
    is_current_question_loaded: false,
    is_current_question_fetch_started: false,
    is_current_answer_fetch_started: false,
    checking_result: {},
    last_question_id: 0,
    error: false,
    success: false,
    selected_question: null,
};

export const questionsSlice = redux.createSlice({
    name: "questions",
    initialState,
    reducers: {
        skipQuestion: (state, action) => {
            state.questions[action.payload].status = 
                QuestionStatus.SKIPPED;
        },
        newQuestion: (state) => {
            state.is_current_answer_loaded = false;
            state.is_current_question_loaded = false;
            state.is_current_answer_fetch_started = false;
            state.is_current_question_fetch_started = false;
            state.checking_result = {};
            if (state.selected_question !== null) { 
                state.selected_question = state.selected_question + 1;
            }
            state.error = false;
            state.success = false;
        },
        selectQuestion: (state, action) => {
            state.selected_question = action.payload;
        }
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
                state.selected_question = state.last_question_id;
            })
            .addCase(Features.fetchRandomQuestion.rejected, 
            (state, action) => {
                state.is_current_question_loaded = true;
                state.error = action.payload;
                state.success = false;
            })
            .addCase(Features.checkAnswer.pending, (state) => {
                state.is_current_answer_fetch_started = true;
                state.error = false;
                state.success = false;
            })
            .addCase(Features.checkAnswer.rejected, (state, action) => {
                state.is_current_answer_loaded = true;
                state.error = action.payload;
                state.success = false;
            })
            .addCase(Features.checkAnswer.fulfilled, (state, action) => {
                state.is_current_answer_loaded = true;
                state.error = false;
                state.success = true;
                state.checking_result = action.payload;
                if (state.checking_result) {
                    state.questions[state.last_question_id].status = 
                        QuestionStatus.SOLVED;
                } else {
                    state.questions[state.last_question_id].status =
                        QuestionStatus.FAILED;
                }
            })
    }
})

export const { skipQuestion, newQuestion, selectQuestion } = 
    questionsSlice.actions;
