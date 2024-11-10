import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const baseQuery = fetchBaseQuery({
  baseUrl: 'http://127.0.0.1:8000/api/',
});

const apiSlice = createApi({
  baseQuery: baseQuery,
  endpoints: (builder) => ({
    getInstitutions: builder.query({
      query: () => 'institutions/',
    }),
    getAcademicYear: builder.query({
      query: () => 'academic-years/',
    }),
  }),
});

export const { useGetInstitutionsQuery, useGetAcademicYearQuery } = apiSlice;
export default apiSlice;
