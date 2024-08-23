import { configureStore } from '@reduxjs/toolkit'
import { authSlice } from '../processes/user';
import { questionsSlice } from '../processes/questions/questionsSlice';

export const store = configureStore({
    reducer: {
        auth: authSlice.reducer,
        questions: questionsSlice.reducer,
    }
});

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = ReturnType<typeof store.dispatch>
