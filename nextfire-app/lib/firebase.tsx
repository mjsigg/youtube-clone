// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { FirebaseStorage } from "firebase/storage"
import { Firestore } from "firebase/firestore"
import { getAuth } from "firebase/auth"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseApp = initializeApp ({
  apiKey: "AIzaSyB8GYyd9Kyjjionc6KvQpkqNx23wuE8jSQ",
  authDomain: "fir-react-next-demo.firebaseapp.com",
  projectId: "fir-react-next-demo",
  storageBucket: "fir-react-next-demo.appspot.com",
  messagingSenderId: "81933844308",
  appId: "1:81933844308:web:4365dafbbda25f90dad2c1",
  measurementId: "G-KR8VN4HKSX"
});

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const auth = getAuth(firebaseApp);


