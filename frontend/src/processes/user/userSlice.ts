import * as redux from "@reduxjs/toolkit";
import * as Features from "../../features/index";

interface InitialStateType {
    loading: boolean;
    userInfo: any;
    userToken: string|null;
    userInfoFetchingStarted: boolean;
    userTokenFetchingStarted: boolean;
    everythingLoaded2: boolean;
    everythingLoaded: boolean;
    error: any;
    success: any;
}

const initialState: InitialStateType = {
    loading: false,
    everythingLoaded: false,
    everythingLoaded2: false,
    userInfoFetchingStarted: false, 
    userTokenFetchingStarted: false,
    userInfo: null,
    userToken: null,
    error: false,
    success: false,
};

export const authSlice = redux.createSlice({
    name: 'auth',
    initialState,
    reducers: {
        logout: (state) => {
            state.userInfo = {};
            state.userToken = null;
            state.error = false;
            state.success = false;
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(Features.signInUser.pending, (state) => {
                state.loading = true;
                state.error = false;
                state.success = false;
                state.userTokenFetchingStarted = true;
            })
            .addCase(Features.signInUser.fulfilled, (state, action) => {
                state.loading = false;
                state.error = false;
                state.success = true;
                state.userToken = action.payload;
                state.everythingLoaded2 = true;
            })
            .addCase(Features.signInUser.rejected, (state, action) => {
                console.log(action);
                state.loading = false;
                state.error = action.payload;
                state.success = false;
                state.everythingLoaded2 = true;
            })
            .addCase(Features.fetchUserInfo.pending, (state) => {
                state.loading = true;
                state.error = false;
                state.success = false;
                state.userInfoFetchingStarted = true;
            })
            .addCase(Features.fetchUserInfo.fulfilled, (state, action) => {
                state.loading = false;
                state.success = true;
                state.everythingLoaded = true;
                state.userInfo = action.payload;
            })
            .addCase(Features.fetchUserInfo.rejected, (state, action) => {
                state.loading = false;
                state.success = false;
                state.everythingLoaded = true;
                state.error = action.payload;
            })
            .addCase(Features.signUpUser.pending, (state) => {
                state.loading = true;
                state.error = false;
                state.success = false;
            })
            .addCase(Features.signUpUser.fulfilled, (state, action) => {
                state.loading = false;
                state.error = false;
                state.success = true;
                state.userInfo = action.payload;
            })
            .addCase(Features.signUpUser.rejected, (state, action) => {
                state.loading = false;
                state.success = false;
                state.error = action.payload;
            })
    }
});  

export const { logout } = authSlice.actions; 
