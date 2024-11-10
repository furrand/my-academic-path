import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '@/features/counter/counterSlice';
import apiSlice from './api/apiSlice';
import userReducer from '@/features/user/userSlice';
import institutionsReducer from '@/features/institutions/institutionsSlice';

const store = configureStore({
  reducer: {
    [apiSlice.reducerPath]: apiSlice.reducer,
    counter: counterReducer,
    institutions: institutionsReducer,
    user: userReducer,
  },
  middleware: (getdefaultMiddleware) =>
    getdefaultMiddleware().concat(apiSlice.middleware),
  devTools: true,
});

export default store;
