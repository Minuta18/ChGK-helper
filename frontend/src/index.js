import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import MainPage from './pages/main_page.js';
import LoginPage from './pages/login_page.js';
import RegisterPage from './pages/register_page.js';
import { MoreQuestionsPage, QuestionsPage } from './pages/questions_page.js';
import SettingsPage from './pages/settings.js';
import { CookiesProvider } from 'react-cookie';

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
        element: <MoreQuestionsPage />,
    },
    {
        path: '/settings',
        element: <SettingsPage/>,
    },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <CookiesProvider>
            <RouterProvider router={ router } />
        </CookiesProvider>
    </React.StrictMode>
);
