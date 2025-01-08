let hisdem = 1;
$(document).ready(function () {
  $("#form_main").submit(function (event) {
    event.preventDefault(); // Prevent the form from submitting via the browser
    var formData = $("#form_main").serialize();
    $.ajax({
      type: "POST",
      url: "/predict",
      data: formData,
      success: function (response) {
        $("#title").css("display", "block");
        if (response["prediction_text"] == "low risk") {
          $("#risk_img").attr("src", "/static/Images/low_risk.png");
          $("#response").css("color", "green");
          $("#response").text("Rủi ro thấp");
          $("#Mota").html(
            "Mô tả: <Br>Ở mức rủi ro thấp, sức khỏe của bà mẹ được đánh giá là ổn định. Các chỉ số y tế như huyết áp, nhịp tim, đường huyết, BMI đều nằm trong khoảng an toàn. Bà mẹ không có yếu tố nguy cơ cao đối với các biến chứng thai kỳ."
          );
          $("#KhuyenNghi").html(
            "Khuyến nghị:<br>Duy trì lối sống lành mạnh, bao gồm chế độ ăn uống cân bằng và vận động nhẹ nhàng.<Br> Tiếp tục tham gia các buổi kiểm tra thai kỳ định kỳ để đảm bảo sức khỏe."
          );
        } else if (response["prediction_text"] == "mid risk") {
          $("#risk_img").attr("src", "/static/Images/medium_risk.png");
          $("#response").css("color", "yellow");
          $("#response").text("Rủi ro trung bình");
          $("#Mota").html(
            "Mô tả: <Br>Mức rủi ro trung bình cho thấy một số dấu hiệu có thể gây ảnh hưởng đến sức khỏe bà mẹ, chẳng hạn như:<Br> Huyết áp hơi cao hoặc thấp hơn bình thường.<Br>Nhịp tim hoặc chỉ số đường huyết có xu hướng không ổn định.<Br> Mặc dù các yếu tố này chưa gây nguy hiểm ngay lập tức, nhưng cần được theo dõi và điều chỉnh kịp thời."
          );
          $("#KhuyenNghi").html(
            "Khuyến nghị:<br>Tham khảo ý kiến bác sĩ để kiểm tra sức khỏe chi tiết hơn.<Br>Theo dõi các chỉ số y tế thường xuyên qua ứng dụng hoặc thiết bị đo.<Br>Điều chỉnh chế độ dinh dưỡng, nghỉ ngơi hợp lý, tránh căng thẳng."
          );
        } else if (response["prediction_text"] == "high risk") {
          $("#risk_img").attr("src", "/static/Images/high_risk.png");
          $("#response").css("color", "red");
          $("#response").text("Rủi ro cao");
          $("#Mota").html(
            "Mô tả: <Br>Mức rủi ro cao cho thấy bà mẹ đang đối mặt với các yếu tố nguy hiểm tiềm tàng, bao gồm:<Br>Huyết áp cao nghiêm trọng (có nguy cơ tiền sản giật).<Br>Nhịp tim bất thường hoặc nhịp nhanh.<Br>Chỉ số đường huyết rất cao (dấu hiệu của tiểu đường thai kỳ).<Br>BMI quá cao (béo phì) hoặc quá thấp (suy dinh dưỡng), ảnh hưởng đến sự phát triển của thai nhi.<Br>Tình trạng này yêu cầu can thiệp y tế khẩn cấp để giảm thiểu nguy cơ biến chứng cho mẹ và bé."
          );
          $("#KhuyenNghi").html(
            "Khuyến nghị:<br>Lập tức đến cơ sở y tế hoặc liên hệ bác sĩ chuyên khoa để được hỗ trợ.Cần giám sát chặt chẽ sức khỏe bằng các thiết bị y tế.<Br>Thực hiện theo hướng dẫn điều trị của bác sĩ, bao gồm chế độ thuốc men, dinh dưỡng và nghỉ ngơi phù hợp.<Br><Br>"
          );
        }
        $("#history-list").prepend(
          `<li>Chuẩn đoán ${hisdem}  Độ rủi ro: ${response["prediction_text"]} </li>`
        );

        hisdem += 1;
      },
      error: function (error) {
        // Handle any errors that occurred during the request
        console.error("Error submitting form:", error);
      },
    });
  });
});

const samples = [
  {
    Age: 35,
    SystolicBP: 120,
    DiastolicBP: 60,
    BS: 6.1,
    BodyTemp: 98,
    HeartRate: 76,
  },
  {
    Age: 30,
    SystolicBP: 120,
    DiastolicBP: 80,
    BS: 6.9,
    BodyTemp: 101,
    HeartRate: 76,
  },
  {
    Age: 35,
    SystolicBP: 140,
    DiastolicBP: 90,
    BS: 7.0,
    BodyTemp: 98.4,
    HeartRate: 85,
  },
  {
    Age: 40,
    SystolicBP: 150,
    DiastolicBP: 95,
    BS: 7.5,
    BodyTemp: 98.7,
    HeartRate: 90,
  },
];

$(document).ready(function () {
  $("#sample-list li").on("click", function () {
    var sampleValue = $(this).data("value");

    // Populate the form with the selected sample data
    var sample = samples[sampleValue - 1]; // Adjust for zero-based index
    $("#Age").val(sample.Age);
    $("#SystolicBP").val(sample.SystolicBP);
    $("#DiastolicBP").val(sample.DiastolicBP);
    $("#BS").val(sample.BS);
    $("#BodyTemp").val(sample.BodyTemp);
    $("#HeartRate").val(sample.HeartRate);
  });
});
