import React from "react";
import { 
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import { Provider } from 'react-redux'

import { IndexPage } from "../pages/index/index";
import store from "./store";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <IndexPage />,
    }
]);

export default function App() {
    return <>
        <Provider store={store}>
            <RouterProvider router={router} />
        </Provider>
    </>;
}
