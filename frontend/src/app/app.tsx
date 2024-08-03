import React from "react";
import { 
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import { Provider } from "react-redux"

import { IndexPage } from "../pages/index/index";
import { SignUpPage } from "../pages/signUp/index";
import { SignInPage } from "../pages/signIn/index";
import { GamePage } from "../pages/gamePage";
import { store } from "./store";

import "./styles/index.css";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <IndexPage />,
    },
    {
        path: "/play",
        element: <GamePage />,
    },
    {
        path: "/auth/sign-up",
        element: <SignUpPage />,
    },
    {
        path: "/auth/sign-in",
        element: <SignInPage />,
    }
]);

export default function App() {
    return <>
        <Provider store={store}>
            <RouterProvider router={router} />
        </Provider>
    </>;
}
