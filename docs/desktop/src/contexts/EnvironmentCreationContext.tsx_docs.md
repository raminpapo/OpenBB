# Documentation: desktop/src/contexts/EnvironmentCreationContext.tsx

## File Metadata
- **Path**: `desktop/src/contexts/EnvironmentCreationContext.tsx`
- **Size**: 1,041 characters, 31 lines
- **Words**: 94
- **Extension**: .tsx
- **Classification**: Text file

## Original Source

```tsx
import { createContext, useContext, useState } from 'react';
import type { ReactNode, FC } from 'react';

interface EnvironmentCreationContextType {
  isCreatingEnvironment: boolean;
  setIsCreatingEnvironment: (isCreating: boolean) => void;
}

const EnvironmentCreationContext = createContext<EnvironmentCreationContextType | undefined>(undefined);

export const useEnvironmentCreation = () => {
  const context = useContext(EnvironmentCreationContext);
  if (context === undefined) {
    throw new Error('useEnvironmentCreation must be used within an EnvironmentCreationProvider');
  }
  return context;
};

interface EnvironmentCreationProviderProps {
  children: ReactNode;
}

export const EnvironmentCreationProvider: FC<EnvironmentCreationProviderProps> = ({ children }) => {
  const [isCreatingEnvironment, setIsCreatingEnvironment] = useState(false);

  return (
    <EnvironmentCreationContext.Provider value={{ isCreatingEnvironment, setIsCreatingEnvironment }}>
      {children}
    </EnvironmentCreationContext.Provider>
  );
}; 
```

## High-Level Overview

This is a .tsx file containing 31 lines of code.

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 3
**Imports**: 2


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `type`

## Notes
- Generated: 2025-11-18T07:54:35.147982
- Generator: World's Best Repo Book Generator v1.0.0
