import '../flutter_flow/flutter_flow_calendar.dart';
import '../flutter_flow/flutter_flow_theme.dart';
import '../flutter_flow/flutter_flow_util.dart';
import 'package:flip_card/flip_card.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:google_fonts/google_fonts.dart';

class JournalWidget extends StatefulWidget {
  const JournalWidget({
    Key? key,
    this.appointmentDetails,
    this.date,
  }) : super(key: key);

  final DateTime? appointmentDetails;
  final bool? date;

  @override
  _JournalWidgetState createState() => _JournalWidgetState();
}

class _JournalWidgetState extends State<JournalWidget> {
  DateTimeRange? calendarSelectedDay;
  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    calendarSelectedDay = DateTimeRange(
      start: DateTime.now().startOfDay,
      end: DateTime.now().endOfDay,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      backgroundColor: FlutterFlowTheme.of(context).primaryBackground,
      appBar: AppBar(
        backgroundColor: FlutterFlowTheme.of(context).primaryBackground,
        automaticallyImplyLeading: false,
        leading: InkWell(
          onTap: () async {
            Navigator.pop(context);
          },
          child: Icon(
            Icons.chevron_left_rounded,
            color: FlutterFlowTheme.of(context).grayLight,
            size: 32,
          ),
        ),
        title: Text(
          'DailyJournal',
          style: FlutterFlowTheme.of(context).title3.override(
                fontFamily: 'Outfit',
                fontSize: 30,
                fontWeight: FontWeight.bold,
              ),
        ),
        actions: [],
        centerTitle: true,
        elevation: 0,
      ),
      body: Column(
        mainAxisSize: MainAxisSize.max,
        children: [
          Stack(
            children: [
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(16, 0, 16, 0),
                child: Row(
                  mainAxisSize: MainAxisSize.max,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      'Select a day to start Journaling',
                      style: FlutterFlowTheme.of(context).bodyText1.override(
                            fontFamily: 'Outfit',
                            color: Color(0xFF2E3339),
                          ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          FlutterFlowCalendar(
            color: FlutterFlowTheme.of(context).background,
            weekFormat: false,
            weekStartsMonday: true,
            onChange: (DateTimeRange? newSelectedDate) async {
              calendarSelectedDay = newSelectedDate;
              if (widget.date!) {
                await Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => JournalWidget(),
                  ),
                );
              }
              setState(() {});
            },
            titleStyle: TextStyle(
              fontWeight: FontWeight.w600,
            ),
            dayOfWeekStyle: TextStyle(),
            dateStyle: TextStyle(),
            selectedDateStyle: TextStyle(),
            inactiveDateStyle: TextStyle(),
          ),
          FlipCard(
            fill: Fill.fillBack,
            direction: FlipDirection.HORIZONTAL,
            speed: 400,
            front: Container(
              width: 374.5,
              height: 386.4,
              decoration: BoxDecoration(
                color: Color(0xFFFBFBFB),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(
                  width: 3,
                ),
              ),
              child: Align(
                alignment: AlignmentDirectional(0, 0),
                child: Text(
                  'Write your thoughts here..\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',
                  style: FlutterFlowTheme.of(context).bodyText1.override(
                        fontFamily: 'Outfit',
                        color: FlutterFlowTheme.of(context).darkBackground,
                        fontWeight: FontWeight.w600,
                      ),
                ),
              ),
            ),
            back: Container(
              width: 100,
              height: 100,
              decoration: BoxDecoration(
                color: FlutterFlowTheme.of(context).tertiaryColor,
                borderRadius: BorderRadius.circular(12),
              ),
              child: Align(
                alignment: AlignmentDirectional(0, 0),
                child: Text(
                  'Back',
                  style: FlutterFlowTheme.of(context).bodyText1.override(
                        fontFamily: 'Outfit',
                        color: FlutterFlowTheme.of(context).primaryText,
                      ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
