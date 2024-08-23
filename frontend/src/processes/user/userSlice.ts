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
    settings: {
        loading_started: boolean,
        loaded: boolean,
        time_for_reading: number,
        time_for_solving: number,
        time_for_typing: number,
    },
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
    settings: {
        loading_started: false,
        loaded: false,
        time_for_reading: 60,
        time_for_solving: 60,
        time_for_typing: 60,
    },
    
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
            .addCase(Features.fetchUserSettings.pending, (state) => {
                state.settings.loading_started = true;
                state.error = false;
                state.success = false;
            })
            .addCase(Features.fetchUserSettings.rejected, (state, action) => {
                state.settings.loaded = true;
                state.error = action.payload;
                state.success = false;
            })
            .addCase(Features.fetchUserSettings.fulfilled, (state, action) => {
                state.settings.loaded = true;
                state.error = false;
                state.success = true;
                state.settings.time_for_reading = 
                    action.payload.time_for_reading;
                state.settings.time_for_solving = 
                    action.payload.time_for_solving;
                state.settings.time_for_typing = 
                    action.payload.time_for_typing;
            })
    }
});  

export const { logout } = authSlice.actions; 
