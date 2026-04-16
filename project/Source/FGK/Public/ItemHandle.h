#pragma once
#include "CoreMinimal.h"
#include "ItemHandle.generated.h"

class UInventoryComponent;

USTRUCT(BlueprintType)
struct FGK_API FItemHandle {
    GENERATED_BODY()
public:
    UPROPERTY(BlueprintReadWrite, EditAnywhere, SaveGame, meta=(AllowPrivateAccess=true))
    int32 ID;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, SaveGame, meta=(AllowPrivateAccess=true))
    int32 Payload;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Export, meta=(AllowPrivateAccess=true))
    TWeakObjectPtr<UInventoryComponent> Owner;
    
    FItemHandle();
};

