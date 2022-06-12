import 'package:flutter/material.dart';
import 'package:toxicapp/drawer.dart';
import 'package:toxicapp/credit_body.dart';
import 'package:toxicapp/toxic_body.dart';

class ToxicApp extends StatefulWidget {
  final ValueChanged<int> changePage;
  final int index;
  const ToxicApp({required this.changePage, required this.index, Key? key})
      : super(key: key);

  @override
  State<ToxicApp> createState() => _ToxicAppState();
}

class _ToxicAppState extends State<ToxicApp> {
  @override
  Widget build(BuildContext context) {
    final navString = ['Toxic Comment Classification Application', 'Credits'];
    final widgetBody = [const ToxicBody(), const CreditBody()];
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        titleTextStyle: const TextStyle(
            color: Colors.black, fontWeight: FontWeight.bold, fontSize: 40),
        centerTitle: true,
        elevation: 0,
        title: Text(navString[widget.index]),
        iconTheme: const IconThemeData(color: Colors.black),
        backgroundColor: Colors.white,
      ),
      body: widgetBody[widget.index],
      drawer: NavMenu(
        changePage: widget.changePage,
      ),
    );
  }
}
