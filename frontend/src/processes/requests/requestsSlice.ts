import * as redux from "@reduxjs/toolkit";

import * as Entities from "../../entities/index";

type ReqRespType = {
    started: boolean,
    loading: boolean,
    success: boolean,
    error_log: string,
    request: Entities.ApiRequest,
    response: Entities.ApiResponse,
}

type InitialStateType = {
    requests: Array<ReqRespType>
}

const initialState: InitialStateType = {
    requests: [],
}

export const responsesSlice = redux.createSlice({
    name: 'responses',
    initialState,
    reducers: {
        
    }
})
