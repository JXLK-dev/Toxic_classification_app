import 'package:flutter/material.dart';
import 'package:toxicapp/function.dart';
import 'dart:convert';

class ToxicBody extends StatefulWidget {
  const ToxicBody({Key? key}) : super(key: key);

  @override
  State<ToxicBody> createState() => _ToxicBodyState();
}

class _ToxicBodyState extends State<ToxicBody> {
  UIUtilities ui = UIUtilities();
  BackEndUtilities machine = BackEndUtilities();
  String comment = '';
  final models = <String>[
    'Support Vector Machine',
    'Logisitic Regression',
    'RandomForest'
  ];
  int selectedIndex = 0;
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: [
          Text(
            'Please insert comment below',
            style: ui.headerStyle(),
          ),
          ui.constSizedBox(20, 0),
          SizedBox(
            width: 500,
            child: TextField(
              decoration: const InputDecoration(
                hintText: 'Input Comment',
                hintMaxLines: 10,
              ),
              minLines: 1,
              maxLines: 5,
              onChanged: (str) {
                setState(() {
                  comment = str;
                });
              },
            ),
          ),
          ui.constSizedBox(20, 0),
          submitButton(selectedIndex),
          ui.constSizedBox(20, 0),
          Text(
            'Select algorithms',
            style: ui.headerStyle(),
          ),
          ui.constSizedBox(20, 0),
          SizedBox(
            height: 30,
            child: ListView.separated(
                scrollDirection: Axis.horizontal,
                shrinkWrap: true,
                separatorBuilder: ((context, index) => ui.constSizedBox(0, 40)),
                itemCount: 3,
                itemBuilder: (context, index) => modelButton(index)),
          ),
          ui.constSizedBox(30, 0),
          Text(
            'Probability',
            style: ui.headerStyle(),
          ),
          ui.constSizedBox(10, 0),
          if (traits.isNotEmpty)
            SizedBox(
              child: ListView.builder(
                  shrinkWrap: true,
                  itemBuilder: ((context, index) => Text(traits[index])),
                  itemCount: traits.length),
            )
        ],
      ),
    );
  }

  List<String> traits = [];
  bool gotData = false;
  final typeModel = <String>['svm', 'logreg', 'randomforest'];
  Widget submitButton(int index) {
    if (comment.isEmpty) {
      return Text(
        'Comment can\'t be empty',
        style: ui.subHeaderStyle(),
      );
    } else {
      return ElevatedButton(
        onPressed: () async {
          //change (server) into an actual local server after launching python app
          String url =
              'http://(server)/${typeModel[index]}?Query= ${comment.toString()}';
          final response = await machine.getData(url);
          final decodeData = jsonDecode(response) as Map<String, dynamic>;
          gotData = true;
          setState(() {
            traits.add(decodeData['Toxic']);
            traits.add(decodeData['Severe']);
            traits.add(decodeData['Obscene']);
            traits.add(decodeData['Insult']);
            traits.add(decodeData['Threat']);
            traits.add(decodeData['IdenHate']);
          });
        },
        style: ui.button(selectedIndex, index),
        child: const Text(
          'submit',
          style: TextStyle(color: Colors.white),
        ),
      );
    }
  }

  Widget modelButton(int index) {
    return ElevatedButton(
      onPressed: () async {
        setState(() {
          selectedIndex = index;
        });
      },
      style: ui.button(selectedIndex, index),
      child: Text(
        models[index],
        style: const TextStyle(color: Colors.white),
      ),
    );
  }
}
