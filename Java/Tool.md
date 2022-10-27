# Tool

## PDF

## merge pages

core code

```java
import java.io.IOException;

import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfReader;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.kernel.utils.PdfMerger;

public class Merge {
    public static void merge(String path,int fromPage,int toPage) {
        try {
            // input source PDF, reader
            PdfDocument sourcePdf=new PdfDocument(new PdfReader(path));
            //System.out.println("getNumberOfPages >> "+sourcePdf.getNumberOfPages());
            
            //output, writer
            PdfDocument outputDoc=new PdfDocument(new PdfWriter("D:\\test.itext.pdf"));
            PdfMerger merger = new PdfMerger(outputDoc);
            merger.merge(sourcePdf, fromPage, toPage);
            
            merger.close();
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

GUI

```java
public class Launch extends Application {
    String filePath = null;

    @Override
    public void start(final Stage primaryStage) throws Exception {

        FlowPane root = new FlowPane();

        final TextField textField = new TextField();

        Button btnChooseFile = new Button("Choose file");
        btnChooseFile.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                FileChooser fileChooser = new FileChooser();
                FileChooser.ExtensionFilter extFilter = new FileChooser.ExtensionFilter("PDF files (*.pdf)", "*.pdf");
                fileChooser.getExtensionFilters().add(extFilter);
                File file = fileChooser.showOpenDialog(primaryStage);
                String PdfAbsolutePath = file.getAbsolutePath();
                filePath = PdfAbsolutePath;
                textField.setText(PdfAbsolutePath);
            }
        });
        root.getChildren().addAll(textField,btnChooseFile);
        
        final TextField txtPageNo = new TextField();
        Button btnConfirm = new Button("confirm");
        btnConfirm.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                String text = txtPageNo.getText();
                int startPage=Integer.valueOf(text.split("-")[0]);
                int endPage=Integer.valueOf(text.split("-")[1]);
                Merge.merge(filePath, startPage, endPage);
                System.out.println(startPage+" and "+endPage);
            }
        });
        root.getChildren().addAll(txtPageNo,btnConfirm);
        
        Scene scene = new Scene(root, 200, 200);
        primaryStage.setScene(scene);

        // scene size
        primaryStage.setWidth(560);
        primaryStage.setHeight(480);
        primaryStage.setMaxWidth(1024);
        primaryStage.setMaxHeight(768);
        primaryStage.setTitle("PDF editor");
        // show
        primaryStage.show();
    }
}

```
