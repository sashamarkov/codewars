#nullable enable
using System;
​
public interface IDateTimeProvider {
  DateTime Now { get; }
}
​
public class RefundRequest {
  public DateTime PurchaseDate { get; set; }
  public string CustomerEmail { get; set; } = string.Empty;
  public bool IsVip { get; set; }
}
​
public class RefundService {
  private readonly IDateTimeProvider _dateTimeProvider;
  
  
  public RefundService(IDateTimeProvider dateTimeProvider) {
    _dateTimeProvider = dateTimeProvider;
  }
​
  public bool ProcessRefund(RefundRequest request) {
    int daysSincePurchase = (_dateTimeProvider.Now - request.PurchaseDate).Days;
    int refundWindow = request.IsVip ? 60 : 30;
    return daysSincePurchase <= refundWindow;
  }
}