import 'package:flutter/material.dart';
import 'package:toxicapp/function.dart';

class CreditBody extends StatefulWidget {
  const CreditBody({Key? key}) : super(key: key);

  @override
  State<CreditBody> createState() => _CreditBodyState();
}

class _CreditBodyState extends State<CreditBody> {
  UIUtilities ui = UIUtilities();
  Uri github =
      Uri.parse('https://github.com/JXLK-dev/Toxic_classification_app');
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: [
          ui.constSizedBox(),
          Text(
            'Machine Learning Project made by:',
            style: ui.headerStyle(),
          ),
          Text(
            'Jerry - 2440050211',
            style: ui.subHeaderStyle(),
          ),
          Text(
            'Felix Museng - 2440026585',
            style: ui.subHeaderStyle(),
          ),
          Text(
            'Nicole - 2440057501',
            style: ui.subHeaderStyle(),
          ),
          Text(
            'Dave Aurellio Delvino - 2440010012',
            style: ui.subHeaderStyle(),
          ),
          ui.constSizedBox(),
          Text(
            'Reference',
            style: ui.headerStyle(),
          ),
          ui.constSizedBox(),
          Text(
            'Our Github reference',
            style: ui.subHeaderStyle(),
          ),
          ui.constSizedBox(),
          ui.linkButton('Github link', github),
          ui.constSizedBox(),
          Text(
            'IEEE paper reference',
            style: ui.subHeaderStyle(),
          ),
        ],
      ),
    );
  }
}
