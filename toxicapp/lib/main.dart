import 'package:flutter/material.dart';
import 'package:toxicapp/toxic_main_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int index = 0;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: ToxicApp(changePage: changePage, index: index),
    );
  }

  void changePage(int index) {
    setState(() {
      this.index = index;
    });
  }
}
