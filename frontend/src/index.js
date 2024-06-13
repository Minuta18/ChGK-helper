import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import MainPage from './pages/main_page.js';
import LoginPage from './pages/login_page.js';
import RegisterPage from './pages/register_page.js';
import QuestionsPage from './pages/questions_page.js';
import SettingsPage from './pages/settings.js';
import Incorrect_answer from './pages/incorr_answer.js';
import Correct_answer from './pages/corr_answer.js';
import Statistics from './pages/statistics.js'


import './index.css';
import './ui/typography/fonts.css';

const router = createBrowserRouter([
    {
        path: '/',
        element: <MainPage />,
    },
    {
        path: '/auth/login',
        element: <LoginPage />,
    },
    {
        path: '/auth/register',
        element: <RegisterPage />,
    },
    {
        path: '/game',
        element: <QuestionsPage />,
    },
    {
        path: '/settings',
        element: <SettingsPage/>,
    },
    {
        path: '/play/incorr',
        element: <Incorrect_answer/>,
    },
    {
        path: '/play/corr',
        element: <Correct_answer/>,
    },
    {
        path: '/play/stat',
        element: <Statistics stats={[
            '1',
            '2'
        ]}/>
    }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <RouterProvider router={ router } />
    </React.StrictMode>
);
