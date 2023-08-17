// IMPORTANT!!
// Because this React app is running in the same workspace as the API,

// there is no need to set a separate baseURL until you reach deployment.

// Setting a baseURL before you reach deployment will cause errors

// Moments > Nav & Auth > Auth: Creating the SignUp form -Part 1

import axios from "axios";

// axios.defaults.baseURL = "https://pp5api-a60f85b616aa.herokuapp.com/";
axios.defaults.headers.post["Content-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();