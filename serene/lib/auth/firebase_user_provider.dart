import 'package:firebase_auth/firebase_auth.dart';
import 'package:rxdart/rxdart.dart';

class SereneFirebaseUser {
  SereneFirebaseUser(this.user);
  User? user;
  bool get loggedIn => user != null;
}

SereneFirebaseUser? currentUser;
bool get loggedIn => currentUser?.loggedIn ?? false;
Stream<SereneFirebaseUser> sereneFirebaseUserStream() => FirebaseAuth.instance
        .authStateChanges()
        .debounce((user) => user == null && !loggedIn
            ? TimerStream(true, const Duration(seconds: 1))
            : Stream.value(user))
        .map<SereneFirebaseUser>(
      (user) {
        currentUser = SereneFirebaseUser(user);
        return currentUser!;
      },
    );
