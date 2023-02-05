import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: FirebaseOptions(
            apiKey: "AIzaSyB9ALSzM177SWW7P7_EzKcNecOlG3IHw9U",
            authDomain: "serene-b5469.firebaseapp.com",
            projectId: "serene-b5469",
            storageBucket: "serene-b5469.appspot.com",
            messagingSenderId: "1003681459415",
            appId: "1:1003681459415:web:5d55deacdab1e6dabad492",
            measurementId: "G-MVJM4GTKK9"));
  } else {
    await Firebase.initializeApp();
  }
}
