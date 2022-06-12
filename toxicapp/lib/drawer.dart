import 'package:flutter/material.dart';
import 'package:toxicapp/function.dart';

class NavMenu extends StatefulWidget {
  final ValueChanged<int> changePage;
  const NavMenu({required this.changePage, Key? key}) : super(key: key);

  @override
  State<NavMenu> createState() => _NavMenuState();
}

class _NavMenuState extends State<NavMenu> {
  final menu = ['Toxic coments classification', 'Credits'];
  int index = 0;
  UIUtilities ui = UIUtilities();
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView.separated(
        separatorBuilder: ((context, index) => const SizedBox(height: 10)),
        itemCount: 2,
        itemBuilder: (context, index) => ListTile(
          onTap: () {
            setState(() {
              this.index = index;
              widget.changePage(this.index);
              ui.closeDrawer(context);
            });
          },
          title: Text(menu[index]),
        ),
      ),
    );
  }
}
