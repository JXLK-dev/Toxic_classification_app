import 'package:flutter/material.dart';
import 'package:toxicapp/function.dart';

class ToxicBody extends StatefulWidget {
  const ToxicBody({Key? key}) : super(key: key);

  @override
  State<ToxicBody> createState() => _ToxicBodyState();
}

class _ToxicBodyState extends State<ToxicBody> {
  UIUtilities ui = UIUtilities();
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
                comment = str;
              },
            ),
          ),
          ui.constSizedBox(20, 0),
          buttons(-1, 'submit'),
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
                itemBuilder: (context, index) => buttons(index, 'model')),
          ),
          ui.constSizedBox(30, 0),
          ui.constSizedBox(30, 0),
          Text(
            'Probability',
            style: ui.headerStyle(),
          ),
          Container()
        ],
      ),
    );
  }

  Widget buttons(int index, String type) {
    return ElevatedButton(
      onPressed: () {
        setState(() {
          if (type == 'model') {
            selectedIndex = index;
          } else {}
        });
      },
      style: ButtonStyle(
        shape: MaterialStateProperty.resolveWith((states) =>
            RoundedRectangleBorder(borderRadius: BorderRadius.circular(30))),
        side: MaterialStateProperty.resolveWith((states) => BorderSide(
            color: selectedIndex == index ? Colors.black : Colors.white,
            width: 3)),
        backgroundColor:
            MaterialStateProperty.resolveWith((states) => Colors.lightBlue),
      ),
      child: Text(
        type == 'model' ? models[index] : 'submit',
        style: const TextStyle(color: Colors.white),
      ),
    );
  }
}
