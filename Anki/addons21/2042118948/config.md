### Configuration

#### Section card
This is for card related settings

<dl>
  <dt>fontSize</dt>
  <dd>Font Size of the card (<b>29px</b>).</dd>

  <dt>padding</dt>
  <dd>Padding of the card (<b>0.8em</b>). Can be set to 0 to have no space between cards</dd>

  <dt>reverseOrderOnBack</dt>
  <dd>On front page the question is left and on back the answer will be right (makes printing easier) <b>true</b> / false</dd>

  <dt>showBorders</dt>
  <dd>show dotted borders between cards (<b>true</b> / false)</dd>

  <dt>skipQuestionOnBack</dt>
  <dd>On answer card the question is not repeated (<b>true</b> / false)</dd>
</dl>

#### Section output
This is for output related settings

<dl>
  <dt>createHtml</dt>
  <dd>html file is created (<b>true</b> / false)</dd>

  <dt>createPdf</dt>
  <dd>pdf file is created (<b>true</b> / false)</dd>

  <dt>filename</dt>
  <dd>filename: <b>papercard_{deck}_%y%m%d</b><br/>
    - variable {deck} might be used for the current exported deck<br/>
    - %y%m%d date formatted string
  </dd>

  <dt>path</dt>
  <dd>Directory, where output should be stored. <b>It must exist!</b>:<br/>
    - either constant <b>download</b><br/>
    - or relative path to User Home (MyAnki)<br/>
    - or absolute path (use / instead of \)<br/>
    &nbsp;&nbsp;- Windows: C:/Users/&lt;CurrentUser&gt;/MyAnki<br/>
    &nbsp;&nbsp;- Linux: /home/&lt;CurrentUser&gt;/MyAnki
  </dd>
</dl>

#### Section paper
This is for paper and printing settings

<dl>
  <dt>cardsPerCol</dt>
  <dd>Number of cards which are displayed vertically (<b>4</b>)</dd>

  <dt>cardsPerRow</dt>
  <dd>Number of cards which are displayed horizontal (<b>4</b>)</dd>

  <dt>format</dt>
  <dd>Paper format for your region (<b>A4</b> / letter)</dd>

  <dt>orientation</dt>
  <dd>Paper orientation: (<b>landscape</b> / portrait)</dd>
</dl>
